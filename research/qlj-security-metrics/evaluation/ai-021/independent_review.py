"""CLI exercise with a separate, explicit binary-matrix row reduction.

No calculator imports and no test_metrics.py reads. All writes stay beside this file.
"""
import datetime
import hashlib
import itertools
import json
import platform
import subprocess
import sys
from pathlib import Path

DEST = Path(__file__).resolve().parent
SOURCE = DEST.parents[1] / 'runtime_metrics.py'

def matrix_for(table, n, degree, side):
    terms = [s for k in range(degree+1) for s in itertools.combinations(range(n), k)]
    selected = [x for x, value in enumerate(table) if value == (1 if side == 'f' else 0)]
    matrix = [[int(all((x >> bit) & 1 for bit in term)) for term in terms] for x in selected]
    return matrix, len(terms)

def rank(matrix, columns):
    # Dense list-of-bits Gauss-Jordan elimination, left to right; unlike source's
    # compressed integer rows, highest-bit pivot dictionary, and witness solver.
    a = [row[:] for row in matrix]
    pivot_row = 0
    for col in range(columns):
        candidate = next((r for r in range(pivot_row, len(a)) if a[r][col]), None)
        if candidate is None:
            continue
        a[pivot_row], a[candidate] = a[candidate], a[pivot_row]
        for r in range(len(a)):
            if r != pivot_row and a[r][col]:
                a[r] = [left ^ right for left, right in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row

def independent_check(table, n, ai):
    evidence = {'reported_status':ai['status'], 'rank_checks':[], 'errors':[]}
    if ai['status'] != 'exact':
        evidence['action'] = 'No exact value or witness claimed; verify nonconstant input exceeds search budget.'
        evidence['budget_stop_consistent'] = n > 6 and len(set(table)) > 1
        if not evidence['budget_stop_consistent']:
            evidence['errors'].append('not_computed inconsistent with declared budget')
        return evidence
    for check in ai['rank_checks']:
        matrix, columns = matrix_for(table, n, check['degree'], check['annihilates'])
        r = rank(matrix, columns)
        computed = {'degree':check['degree'], 'annihilates':check['annihilates'],
                    'rows':len(matrix), 'columns':columns, 'rank':r, 'nullity':columns-r}
        match = computed == check
        evidence['rank_checks'].append({'reported':check,'independent':computed,'match':match})
        if not match:
            evidence['errors'].append('rank record mismatch')
    value = ai['value']
    all_lower = []
    for d in range(value):
        for side in ('f','f+1'):
            matrix, columns = matrix_for(table,n,d,side)
            r = rank(matrix,columns)
            all_lower.append({'degree':d,'annihilates':side,'rank':r,'columns':columns,'full_column_rank':r==columns})
    evidence['lower_degree_both_sides'] = all_lower
    if not all(row['full_column_rank'] for row in all_lower):
        evidence['errors'].append('claimed minimum not justified by lower-degree ranks')
    masks = ai['monomial_masks']
    witness = [sum(all((x>>b)&1 for b in range(n) if (mask>>b)&1) for mask in masks)%2 for x in range(1<<n)]
    degree = max((mask.bit_count() for mask in masks),default=0)
    product = [g*(v if ai['annihilates']=='f' else 1-v) for g,v in zip(witness,table)]
    evidence['witness'] = {'nonzero':any(witness),'matches_reported_table':witness==ai['witness_table'],
        'degree_from_masks':degree,'degree_matches_AI':degree==value,'product_all_zero':not any(product),
        'degree_nonnegative_bound':value>=0}
    if not all(evidence['witness'][k] for k in ('nonzero','matches_reported_table','degree_matches_AI','product_all_zero','degree_nonnegative_bound')):
        evidence['errors'].append('witness verification failed')
    if ai['method'] == 'constant_function_identity':
        evidence['constant_identity_checked'] = len(set(table))==1 and value==0 and masks==[0] and ai['rank_checks']==[]
        if not evidence['constant_identity_checked']:
            evidence['errors'].append('constant identity invalid')
    else:
        # Check log covers every lower degree on both sides, and the stated
        # annihilator side has a null vector at the claimed winning degree.
        present = {(c['degree'],c['annihilates']) for c in ai['rank_checks']}
        evidence['all_lower_degree_records_present'] = all((d,side) in present for d in range(value) for side in ('f','f+1'))
        matrix, columns = matrix_for(table,n,value,ai['annihilates'])
        evidence['winning_degree_nullity'] = columns-rank(matrix,columns)
        if not evidence['all_lower_degree_records_present'] or evidence['winning_degree_nullity']<=0:
            evidence['errors'].append('search trace incomplete or no winning nullspace')
    return evidence

cases = [
    ('n2-and',2,[0,0,0,1]),
    ('n4-paired-bent',4,[(((x>>3)&1)*((x>>1)&1)) ^ (((x>>2)&1)*(x&1)) for x in range(16)]),
    ('n7-zero',7,[0]*128),
    ('n7-one',7,[1]*128),
    ('n7-parity',7,[bin(x).count('1')%2 for x in range(128)]),
]
report = {'review':'AI output incremental independent CLI review',
          'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'environment':{'python':sys.executable,'version':platform.python_version()},
          'source':str(SOURCE),'source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'independence':'No imports from calculator. Dense binary Gauss-Jordan with leftmost pivots, combination-based monomial basis. No test_metrics.py read.',
          'cases':[]}
for name,n,table in cases:
    inp = DEST/(name+'-input.json')
    out = DEST/(name+'-output.json')
    inp.write_text(json.dumps({'n':n,'m':1,'table':table,'ai':True})+'\n',encoding='utf-8')
    command = [sys.executable,str(SOURCE),'--input',str(inp),'--out',str(out)]
    p = subprocess.run(command,cwd=DEST,capture_output=True,text=True,encoding='utf-8')
    record = {'case':name,'command':command,'command_display':subprocess.list2cmdline(command),
              'cwd':str(DEST),'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr,
              'input_file':str(inp),'output_file':str(out)}
    if p.returncode==0:
        output = json.loads(out.read_text(encoding='utf-8'))
        ai = output['result']['algebraic_immunity']
        record['actual_ai_result'] = ai
        record['independent_verification'] = independent_check(table,n,ai)
        record['passed'] = not record['independent_verification']['errors']
    else:
        record['passed'] = False
    report['cases'].append(record)
report['summary'] = {'CLI_runs':len(cases),'successful_exits':sum(c['exit_code']==0 for c in report['cases']),
    'independent_checks_passed':sum(c['passed'] for c in report['cases']),
    'reported_rank_records_checked':sum(len(c.get('actual_ai_result',{}).get('rank_checks',[])) for c in report['cases'])}
(DEST/'independent-review.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report['summary']))
for c in report['cases']:
    q=c.get('actual_ai_result',{})
    print(c['case'], 'exit='+str(c['exit_code']), 'status='+str(q.get('status')), 'AI='+str(q.get('value')), 'passed='+str(c['passed']))
raise SystemExit(0 if all(c['passed'] for c in report['cases']) else 1)
