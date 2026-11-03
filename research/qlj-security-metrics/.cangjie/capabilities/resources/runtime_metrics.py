"""QLJ finite-table reference calculator, Python 3.10+, independent implementation.

Bit masks use x1 as the most significant input bit, matching book p1.
This program proves only properties of the supplied finite table.
"""
import argparse
import hashlib
import json


def validate(table, n, m=1):
    if type(n) is not int or type(m) is not int or not 1 <= n <= 10 or not 1 <= m <= 8:
        raise ValueError('require integer 1<=n<=10, 1<=m<=8')
    if not isinstance(table, list) or len(table) != 1 << n:
        raise ValueError('table length must equal 2^n')
    if any(type(v) is not int or not 0 <= v < 1 << m for v in table):
        raise ValueError('table entries must be integers in [0,2^m)')


def parity(v):
    return v.bit_count() & 1


def mobius(table):
    a = table[:]
    for k in range((len(a)-1).bit_length()):
        for x in range(len(a)):
            if x & (1 << k):
                a[x] ^= a[x ^ (1 << k)]
    return a


def walsh(table):
    a = [1 - 2*v for v in table]
    step = 1
    while step < len(a):
        for j in range(0, len(a), step*2):
            for k in range(j, j+step):
                u, v = a[k], a[k+step]
                a[k], a[k+step] = u+v, u-v
        step *= 2
    return a


def null_witness(rows, cols):
    """Return a nonzero GF(2) null vector; rows are integer bitmasks."""
    pivots = {}
    for row in rows:
        while row:
            p = row.bit_length()-1
            if p not in pivots:
                pivots[p] = row
                break
            row ^= pivots[p]
    free = next((j for j in range(cols) if j not in pivots), None)
    if free is None:
        return None
    v = 1 << free
    for p in sorted(pivots):
        if parity(pivots[p] & v):
            v |= 1 << p
    return v


def algebraic_immunity(table, n):
    if n > 6:
        return {'status': 'not_computed', 'reason': 'exact AI requires n<=6'}
    for d in range((n+1)//2+1):
        monomials = [mask for mask in range(1 << n) if mask.bit_count() <= d]
        for target in (0, 1):
            # g annihilates f if g vanishes where f=1; or f+1 where f=0.
            rows = [sum(1 << j for j,mask in enumerate(monomials) if x & mask == mask)
                    for x,v in enumerate(table) if v == 1-target]
            coeff = null_witness(rows, len(monomials))
            if coeff is not None:
                masks = [mask for j,mask in enumerate(monomials) if coeff >> j & 1]
                values = [parity(sum(1 << j for j,mask in enumerate(masks) if x & mask == mask))
                          for x in range(1 << n)]
                assert any(values) and all(not values[x] or table[x] == target for x in range(1 << n))
                return {'status': 'exact', 'value': d, 'annihilates': 'f' if target == 0 else 'f+1',
                        'monomial_masks': masks, 'witness_table': values,
                        'optimal': d == (n+1)//2}
    raise AssertionError('AI upper bound failed')


def scalar(table, n, ai=False):
    validate(table, n)
    w = walsh(table)
    anf = mobius(table)
    amplitude = max(map(abs, w))
    ci = n
    for mask in range(1, 1 << n):
        if w[mask]:
            ci = min(ci, mask.bit_count()-1)
    bent = n % 2 == 0 and all(v*v == 1 << n for v in w)
    result = {'weight': sum(table), 'balanced': sum(table) == 1 << (n-1),
              'degree': max((i.bit_count() for i,v in enumerate(anf) if v), default=0),
              'anf_masks': [i for i,v in enumerate(anf) if v],
              'walsh': w, 'nonlinearity': (1 << (n-1))-amplitude//2,
              'correlation_immunity_order': ci,
              'resiliency_order': ci if w[0] == 0 else None, 'bent': bent}
    if bent:
        result['dual_table'] = [int(v < 0) for v in w]
    if ai:
        result['algebraic_immunity'] = algebraic_immunity(table, n)
    return result


def analyze(spec):
    if not isinstance(spec, dict):
        raise ValueError('input must be an object')
    n, m, table = spec.get('n'), spec.get('m',1), spec.get('table')
    validate(table,n,m)
    ai = spec.get('ai',False)
    if type(ai) is not bool:
        raise ValueError('ai must be a JSON boolean')
    if m == 1:
        data = scalar(table,n,ai)
    else:
        if n > 8:
            raise ValueError('vector analysis requires n<=8')
        components = {str(b): scalar([parity(b & v) for v in table],n,ai)
                      for b in range(1,1 << m)}
        ddt = []
        for a in range(1 << n):
            row = [0] * (1 << m)
            for x in range(1 << n):
                row[table[x] ^ table[x ^ a]] += 1
            ddt.append(row)
        delta = max(max(row) for row in ddt[1:])
        witness = next([a,b] for a in range(1,1 << n) for b,v in enumerate(ddt[a]) if v==delta)
        vector_bent = all(c['bent'] for c in components.values())
        ab = n == m and n % 2 == 1 and all(
            v in (0,1 << ((n+1)//2),-(1 << ((n+1)//2)))
            for c in components.values() for v in c['walsh'])
        data = {'components': components, 'nonlinearity': min(c['nonlinearity'] for c in components.values()),
                'ddt': ddt, 'differential_uniformity': delta, 'differential_witness': witness,
                'permutation': n==m and len(set(table))==len(table),
                'binary_pn': n>=m and delta == 1 << (n-m),
                'binary_square_apn': delta==2 if n==m else None,
                'vector_bent': vector_bent,
                'square_almost_bent': ab if n==m else None,
                'resiliency_order': min(c['resiliency_order'] for c in components.values())
                    if all(c['balanced'] for c in components.values()) else None}
    return {'schema_version':1,'verification':'exhaustive_finite_table',
            'convention':'ascending integer index; x1 MSB; XOR difference; unnormalized Walsh',
            'n':n,'m':m,'input_sha256':hashlib.sha256(json.dumps(spec,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
            'result':data}


def paired_bent(n):
    if type(n) is not int or not 2 <= n <= 10 or n % 2:
        raise ValueError('paired Bent requires even integer 2<=n<=10')
    h=n//2
    # f=sum x_i*x_(h+i); x1 is the MSB, as in book example 4.1.
    return {'n':n,'m':1,'table':[parity((x>>h) & (x & ((1<<h)-1))) for x in range(1<<n)]}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--input')
    mode.add_argument('--paired-bent',type=int)
    p.add_argument('--out')
    args = p.parse_args()
    try:
        def unique(pairs):
            d={}
            for k,v in pairs:
                if k in d: raise ValueError('duplicate JSON key: '+k)
                d[k]=v
            return d
        if args.paired_bent is not None:
            spec=paired_bent(args.paired_bent)
        else:
            with open(args.input,encoding='utf-8-sig') as f:
                spec=json.load(f,object_pairs_hook=unique,parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))
        report=analyze(spec)
        report['input']=spec
        result = json.dumps(report,ensure_ascii=False,indent=2)
        if args.out:
            with open(args.out,'x',encoding='utf-8') as f: f.write(result+'\n')
        else: print(result)
    except (ValueError,TypeError,OSError) as e:
        p.exit(2,str(e)+'\n')


if __name__ == '__main__': main()
