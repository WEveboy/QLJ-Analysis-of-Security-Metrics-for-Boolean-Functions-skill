"""Maiorana-McFarland finite construction; coordinates z=(x<<h)|y."""
import argparse
import json
from runtime_metrics import analyze, parity


def construct(spec):
    if not isinstance(spec,dict):
        raise ValueError('spec must be an object')
    h=spec.get('h')
    if type(h) is not int or not 1<=h<=5:
        raise ValueError('require integer 1<=h<=5')
    size=1<<h
    pi,g=spec.get('pi'),spec.get('g')
    if not isinstance(pi,list) or len(pi)!=size or any(type(v) is not int for v in pi) or sorted(pi)!=list(range(size)):
        raise ValueError('pi must be a permutation of 0..2^h-1')
    if not isinstance(g,list) or len(g)!=size or any(type(v) is not int or v not in (0,1) for v in g):
        raise ValueError('g must be a Boolean table of length 2^h')
    table=[parity(x & pi[y]) ^ g[y] for x in range(size) for y in range(size)]
    inv=[0]*size
    for y,v in enumerate(pi): inv[v]=y
    predicted=[size*(1-2*(g[inv[a]] ^ parity(b & inv[a])))
               for a in range(size) for b in range(size)]
    report=analyze({'n':2*h,'m':1,'table':table})
    assert report['result']['walsh']==predicted
    assert report['result']['bent']
    return {'construction':'Maiorana-McFarland','h':h,'pi':pi,'g':g,
            'coordinates':'z=(x<<h)|y; first h variables are x; integer-ascending blocks',
            'function':{'n':2*h,'m':1,'table':table},'analysis':report,
            'certificate':{'inverse_pi':inv,'predicted_walsh':predicted,'matched':True},
            'scope':'finite instance; source theorem provides family proof, not a novelty claim'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',required=True);p.add_argument('--out')
    a=p.parse_args()
    try:
        def unique(pairs):
            d={}
            for k,v in pairs:
                if k in d:raise ValueError('duplicate key: '+k)
                d[k]=v
            return d
        with open(a.input,encoding='utf-8-sig') as f:spec=json.load(f,object_pairs_hook=unique)
        data=json.dumps(construct(spec),ensure_ascii=False,indent=2)
        if a.out:
            with open(a.out,'x',encoding='utf-8') as f:f.write(data+'\n')
        else:print(data)
    except (ValueError,TypeError,OSError) as e:p.exit(2,str(e)+'\n')


if __name__=='__main__':main()
