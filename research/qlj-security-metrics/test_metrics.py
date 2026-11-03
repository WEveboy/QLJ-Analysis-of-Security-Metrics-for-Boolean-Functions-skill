import itertools
import unittest
from runtime_metrics import analyze, scalar, mobius, algebraic_immunity, paired_bent


def brute_walsh(t,n):
    return [sum((-1)**(v+((x&a).bit_count()%2)) for x,v in enumerate(t)) for a in range(1<<n)]


def brute_ai(t,n):
    best=n+1
    for bits in range(1,1 << (1<<n)):
        g=[bits>>x&1 for x in range(1<<n)]
        if all(not (a*b) for a,b in zip(t,g)) or all(not ((1-a)*b) for a,b in zip(t,g)):
            best=min(best,max((i.bit_count() for i,v in enumerate(mobius(g)) if v),default=0))
    return best


class MetricsTests(unittest.TestCase):
    def test_paired_construction_range(self):
        for n in (2,4,6,8,10):
            spec=paired_bent(n)
            r=analyze(spec)['result']
            self.assertTrue(r['bent'])
            self.assertEqual(r['nonlinearity'],(1<<(n-1))-(1<<(n//2-1)))
        for n in (0,1,3,11,True):
            with self.assertRaises(ValueError):paired_bent(n)
    def test_exhaustive_scalar_through_three_variables(self):
        # 4 + 16 + 256 tables; direct sums and distances independently check FWHT.
        for n in (1,2,3):
            for bits in range(1 << (1<<n)):
                t=[bits>>x&1 for x in range(1<<n)]
                r=scalar(t,n,True)
                self.assertEqual(r['walsh'],brute_walsh(t,n))
                self.assertEqual(mobius(mobius(t)),t)
                distances=[sum(v!=(((x&a).bit_count()&1)^c) for x,v in enumerate(t))
                           for a in range(1<<n) for c in (0,1)]
                self.assertEqual(r['nonlinearity'],min(distances))
                self.assertEqual(r['algebraic_immunity']['value'],brute_ai(t,n))

    def test_all_two_by_two_maps(self):
        for t in itertools.product(range(4),repeat=4):
            r=analyze({'n':2,'m':2,'table':list(t)})['result']
            for a,row in enumerate(r['ddt']):
                self.assertEqual(sum(row),4)
                for b,v in enumerate(row):
                    self.assertEqual(v,sum((t[x]^t[x^a])==b for x in range(4)))
                    if a: self.assertEqual(v%2,0)
            self.assertFalse(r['binary_pn'])
            self.assertFalse(r['vector_bent'])

    def test_bent_dual(self):
        t=[((x>>3&1)*(x>>2&1))^((x>>1&1)*(x&1)) for x in range(16)]
        r=scalar(t,4,True)
        self.assertTrue(r['bent']); self.assertEqual(r['nonlinearity'],6)
        self.assertFalse(r['balanced']); self.assertEqual(r['algebraic_immunity']['value'],2)
        self.assertEqual(scalar(r['dual_table'],4)['dual_table'],t)

    def test_ab_gold(self):
        def mul(a,b):
            c=0
            while b:
                if b&1:c^=a
                b>>=1;a<<=1
                if a&8:a^=11
            return c
        t=[mul(mul(x,x),x) for x in range(8)]
        r=analyze({'n':3,'m':3,'table':t})['result']
        self.assertEqual(r['differential_uniformity'],2)
        self.assertEqual(r['nonlinearity'],2)
        self.assertTrue(r['square_almost_bent']);self.assertTrue(r['permutation'])

    def test_coordinates_do_not_suffice(self):
        r=analyze({'n':2,'m':2,'table':[0,0,3,3]})['result']
        self.assertTrue(r['components']['1']['balanced'])
        self.assertTrue(r['components']['2']['balanced'])
        self.assertFalse(r['components']['3']['balanced'])
        self.assertIsNone(r['resiliency_order'])

    def test_parity_and_constants(self):
        self.assertEqual(scalar([x.bit_count()%2 for x in range(16)],4)['resiliency_order'],3)
        for v in (0,1):
            r=scalar([v]*16,4,True)
            self.assertEqual(r['algebraic_immunity']['value'],0)
            self.assertIsNone(r['resiliency_order'])

    def test_ai_budget(self):
        self.assertEqual(algebraic_immunity([0]*128,7)['status'],'not_computed')

    def test_reject_bad_input(self):
        for s in ({'n':True,'table':[0,1]}, {'n':2,'table':[0,1]},
                  {'n':1,'table':[False,1]}, {'n':1,'m':2,'table':[0,4]},
                  {'n':1,'ai':'yes','table':[0,1]}, {'n':11,'table':[]}):
            with self.assertRaises(ValueError):analyze(s)


if __name__=='__main__':unittest.main()
