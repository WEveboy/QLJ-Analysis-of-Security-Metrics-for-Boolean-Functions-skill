"""Independent exhaustive baseline; Python standard library only.

Input indexing: x is an integer, x_0 is its least significant bit.
No project modules, skills, research notes, or expected results are read.
"""
import itertools
import json
from pathlib import Path


def dot(a, x):
    return (a & x).bit_count() & 1


def walsh(truth):
    return [sum((-1) ** (truth[x] ^ dot(a, x)) for x in range(len(truth)))
            for a in range(len(truth))]


def anf(truth):
    coefficients = list(truth)
    n = len(truth).bit_length() - 1
    for i in range(n):
        for mask in range(len(truth)):
            if mask & (1 << i):
                coefficients[mask] ^= coefficients[mask ^ (1 << i)]
    return coefficients


def degree(truth):
    return max((mask.bit_count() for mask, c in enumerate(anf(truth)) if c), default=-1)


def nonlinearity(truth):
    return (len(truth) - max(map(abs, walsh(truth)))) // 2


def monomials(truth):
    return [mask for mask, c in enumerate(anf(truth)) if c]


def algebraic_immunity(truth):
    # Enumerate every nonzero Boolean g, and both h=f and h=f+1.
    candidates = []
    for values in itertools.product((0, 1), repeat=len(truth)):
        if not any(values):
            continue
        for complement in (0, 1):
            if all(not ((truth[x] ^ complement) & values[x]) for x in range(len(truth))):
                candidates.append({"degree": degree(values), "annihilates": "f" if complement == 0 else "f+1",
                                   "truth": list(values), "anf_masks": monomials(values)})
    best = min(item["degree"] for item in candidates)
    return best, [item for item in candidates if item["degree"] == best]


def vector_analysis(table, m):
    size = len(table)
    ddt = []
    for a in range(size):
        row = [0] * (1 << m)
        for x in range(size):
            row[table[x] ^ table[x ^ a]] += 1
        ddt.append(row)
    components = {}
    for b in range(1, 1 << m):
        truth = [dot(b, y) for y in table]
        components[str(b)] = {"truth": truth, "walsh": walsh(truth), "nonlinearity": nonlinearity(truth)}
    n = size.bit_length() - 1
    target = 1 << ((n + 1) // 2)
    is_ab = n == m and n % 2 == 1 and all(
        set(c["walsh"]) <= {0, -target, target} for c in components.values())
    return {"delta": max(max(row) for row in ddt[1:]), "ddt": ddt,
            "nonlinearity": min(c["nonlinearity"] for c in components.values()),
            "almost_bent_square_odd": is_ab, "components": components}


def main():
    f_a = [0, 0, 0, 1]
    ai, annihilators = algebraic_immunity(f_a)
    a = {"n": 2, "truth": f_a, "anf_coefficients": anf(f_a), "anf_masks": monomials(f_a),
         "anf_text": "x_0*x_1", "walsh": walsh(f_a), "nonlinearity": nonlinearity(f_a),
         "algebraic_immunity": ai, "minimum_degree_annihilators": annihilators}
    b = vector_analysis([0, 1, 3, 4, 5, 6, 7, 2], 3)
    parity = [x.bit_count() & 1 for x in range(16)]
    spectrum = walsh(parity)
    # CI order t: every Walsh coefficient of mask weight 1,...,t vanishes.
    ci = max(t for t in range(5) if all(spectrum[mask] == 0 for mask in range(1, 16)
                                                   if mask.bit_count() <= t))
    balanced = sum(parity) == 8
    c = {"n": 4, "truth": parity, "walsh": spectrum, "degree": degree(parity),
         "balanced": balanced, "correlation_immunity_order": ci,
         "resiliency_order": ci if balanced else None}
    d_table = [0, 0, 3, 3]
    output_counts = [d_table.count(y) for y in range(4)]
    d_components = vector_analysis(d_table, 2)["components"]
    d = {"n": 2, "m": 2, "truth": d_table, "output_counts": output_counts,
         "coordinate_balanced": [sum(d_components[str(1 << i)]["truth"]) == 2 for i in range(2)],
         "vector_balanced": len(set(output_counts)) == 1,
         "components": d_components,
         "conclusion": "Balanced coordinates do not imply a balanced vector mapping."}
    results = {"convention": "Input masks and component masks ordered numerically; x_0 is LSB.",
               "A": a, "B": b, "C": c, "D": d}
    destination = Path(__file__).resolve().parent
    (destination / "results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    summary = f"""# Independent baseline results

Computed by `independent_baseline.py` using only the Python standard library.
Input and Walsh masks use integer order, with x_0 as the least significant bit.

| Task | Actual result |
| --- | --- |
| A: n=2, [0,0,0,1] | ANF=x_0*x_1; Walsh={a['walsh']}; NL={a['nonlinearity']}; AI={ai} |
| B: n=m=3, [0,1,3,4,5,6,7,2] | delta={b['delta']}; vector NL={b['nonlinearity']}; Almost Bent={b['almost_bent_square_odd']} |
| C: n=4 parity | balanced={balanced}; CI order={ci}; resiliency order={c['resiliency_order']} |
| D: n=m=2, [0,0,3,3] | both coordinates balanced; vector balanced={d['vector_balanced']}; output multiplicities={output_counts} |

For A, nonzero minimum-degree annihilators of f are 1+x_0, 1+x_1, and x_0+x_1.
There is no degree-one annihilator of f+1. Exhaustive enumeration checks all 15 nonzero g.
The value AI=1 follows from the minimum over annihilators of f and f+1.

For B, every nonzero component has Walsh values in {{0,-4,4}}, the defining square odd-dimensional Almost Bent spectrum.
The full DDT and all component spectra are recorded in results.json.

For C, only Walsh mask 15 has nonzero value 16. All nonzero masks of weights 1 through 3 vanish;
the weight-4 coefficient does not vanish. Therefore the exact CI and resiliency orders are 3.

For D, component mask 3 is identically zero: the two balanced coordinates coincide.
A balanced mapping would require one occurrence of each output, whereas only 0 and 3 occur, twice each.
Thus coordinate balance does not imply vector balance.
"""
    (destination / "RESULTS.md").write_text(summary, encoding="utf-8")
    print(summary)


if __name__ == "__main__":
    main()
