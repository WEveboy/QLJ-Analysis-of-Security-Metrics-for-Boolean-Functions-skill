import itertools
import unittest
from mm_construction import construct


class MMTests(unittest.TestCase):
    def test_all_h2_permutations_and_offsets(self):
        for pi in itertools.permutations(range(4)):
            for g in itertools.product((0,1),repeat=4):
                r=construct({'h':2,'pi':list(pi),'g':list(g)})
                t=r['function']['table']
                direct=[sum((-1)**(v+((a&x).bit_count()%2)) for x,v in enumerate(t)) for a in range(16)]
                self.assertEqual(direct,r['certificate']['predicted_walsh'])
                self.assertEqual(r['analysis']['result']['nonlinearity'],6)

    def test_budget_endpoints(self):
        for h in (1,3,5):
            size=1<<h
            r=construct({'h':h,'pi':list(reversed(range(size))),'g':[x.bit_count()%2 for x in range(size)]})
            self.assertTrue(r['analysis']['result']['bent'])
            self.assertEqual(len(r['function']['table']),1<<(2*h))

    def test_invalid_spec(self):
        for spec in ({'h':True},{'h':0},{'h':6},{'h':2,'pi':[0,0,2,3],'g':[0]*4},
                     {'h':1,'pi':[False,1],'g':[0,1]}, {'h':1,'pi':[0,1],'g':[0,True]},
                     {'h':1,'pi':[0,1],'g':[0]},[]):
            with self.assertRaises(ValueError):construct(spec)


if __name__=='__main__':unittest.main()
