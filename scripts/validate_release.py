"""Run release checks and write a new structured command log (standard library)."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile
import time

ROOT=Path(__file__).resolve().parents[1]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',required=True,help='new report path; never overwrite')
    args=p.parse_args()
    # Reserve the log before running, so a pre-existing report is never replaced.
    with open(args.out,'x',encoding='utf-8') as output:
        records=[]
        def run(label,argv):
            started=datetime.now(timezone.utc).isoformat()
            tick=time.monotonic()
            proc=subprocess.run([sys.executable,*argv],cwd=ROOT,text=True,encoding='utf-8',
                                errors='replace',capture_output=True)
            records.append(dict(stage=label,started_utc=started,elapsed_seconds=time.monotonic()-tick,
                                command=[sys.executable,*argv],exit_code=proc.returncode,
                                stdout=proc.stdout,stderr=proc.stderr))
            return proc
        run('unit_tests',['-m','unittest','discover','-s','skills/qlj-security-metrics/resources','-p','test_*.py','-v'])
        run('repository_integrity',['scripts/check_repository.py'])
        smoke={}
        with tempfile.TemporaryDirectory(prefix='qlj-validation-') as tmp:
            for name,script,spec in [
                ('gold','runtime_metrics.py',ROOT/'examples/gold-3.json'),
                ('bent','runtime_metrics.py',ROOT/'examples/bent-4.json'),
                ('mm','mm_construction.py',ROOT/'examples/mm-4.json')]:
                proc=run(name,['skills/qlj-security-metrics/resources/'+script,'--input',str(spec)])
                try:
                    result=json.loads(proc.stdout)
                    if name=='gold':smoke[name]=result['result']['differential_uniformity']==2 and result['result']['nonlinearity']==2
                    elif name=='bent':smoke[name]=result['result']['bent'] and result['result']['algebraic_immunity']['value']==2 and bool(result['result']['algebraic_immunity']['rank_checks'])
                    else:smoke[name]=result['certificate']['matched'] and result['analysis']['result']['nonlinearity']==6
                except (ValueError,KeyError,TypeError):smoke[name]=False
            bad=Path(tmp)/'bad.json'
            bad.write_text('{"h":2,"pi":[0,0,2,3],"g":[0,0,0,0]}',encoding='utf-8')
            destination=Path(tmp)/'must-not-exist.json'
            proc=run('invalid_mm',['skills/qlj-security-metrics/resources/mm_construction.py','--input',str(bad),'--out',str(destination)])
            smoke['invalid_mm']=proc.returncode==2 and not destination.exists()
        success=all(r['exit_code']==(2 if r['stage']=='invalid_mm' else 0) for r in records) and all(smoke.values())
        fingerprints={f.name:hashlib.sha256(f.read_bytes()).hexdigest()
                      for f in (ROOT/'skills/qlj-security-metrics/resources').glob('*.py')}
        report=dict(schema_version=1,status='passed' if success else 'failed',
                    environment=dict(python=sys.version,platform=platform.platform()),
                    runtime_sha256=fingerprints,commands=records,smoke_assertions=smoke,
                    limitation='command evidence and internal hashes; not a signature or full-book proof')
        json.dump(report,output,ensure_ascii=False,indent=2)
        output.write('\n')
    print(report['status'])
    return 0 if success else 1


if __name__=='__main__':sys.exit(main())
