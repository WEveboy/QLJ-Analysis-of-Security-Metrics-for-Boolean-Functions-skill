# Independent baseline results

Computed by `independent_baseline.py` using only the Python standard library.
Input and Walsh masks use integer order, with x_0 as the least significant bit.

| Task | Actual result |
| --- | --- |
| A: n=2, [0,0,0,1] | ANF=x_0*x_1; Walsh=[2, 2, 2, -2]; NL=1; AI=1 |
| B: n=m=3, [0,1,3,4,5,6,7,2] | delta=2; vector NL=2; Almost Bent=True |
| C: n=4 parity | balanced=True; CI order=3; resiliency order=3 |
| D: n=m=2, [0,0,3,3] | both coordinates balanced; vector balanced=False; output multiplicities=[2, 0, 0, 2] |

For A, nonzero minimum-degree annihilators of f are 1+x_0, 1+x_1, and x_0+x_1.
There is no degree-one annihilator of f+1. Exhaustive enumeration checks all 15 nonzero g.
The value AI=1 follows from the minimum over annihilators of f and f+1.

For B, every nonzero component has Walsh values in {0,-4,4}, the defining square odd-dimensional Almost Bent spectrum.
The full DDT and all component spectra are recorded in results.json.

For C, only Walsh mask 15 has nonzero value 16. All nonzero masks of weights 1 through 3 vanish;
the weight-4 coefficient does not vanish. Therefore the exact CI and resiliency orders are 3.

For D, component mask 3 is identically zero: the two balanced coordinates coincide.
A balanced mapping would require one occurrence of each output, whereas only 0 and 3 occur, twice each.
Thus coordinate balance does not imply vector balance.
