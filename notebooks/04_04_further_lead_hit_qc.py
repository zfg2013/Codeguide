import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    hydrophobic = set("AILMFWV")
    charged = {"K": 1, "R": 1, "D": -1, "E": -1}
    hits = ["AKLV", "KKLL", "DDWY", "GPGS", "AVAV"]
    rows = []
    for peptide in hits:
        charge = sum(charged.get(aa, 0) for aa in peptide)
        hydrophobicity = sum(aa in hydrophobic for aa in peptide) / len(peptide)
        diversity = len(set(peptide)) / len(peptide)
        pass_qc = abs(charge) <= 2 and hydrophobicity <= 0.75 and diversity >= 0.5
        rows.append((peptide, charge, hydrophobicity, diversity, pass_qc))
    sample_values = [1 if row[-1] else 0 for row in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {pep} | {charge} | {hydro:.2f} | {diversity:.2f} | {pass_qc} |" for pep, charge, hydro, diversity, pass_qc in rows)
    mo.md(f"""
# Further Lead Hit QC

Short intro: QC peptide hits for diversity, charge, hydrophobicity, and length.

## Learning goals
Apply clear pass/fail gates before selection.

## Background
The QC rules are synthetic and inspectable.

## Interactive example
| Peptide | Charge | Hydrophobic fraction | Diversity | Pass QC |
| --- | ---: | ---: | ---: | --- |
{table}

## Exercise
Tighten the hydrophobicity threshold to 0.50.

## Notes for future editing
Add synthesis and liability flags later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
