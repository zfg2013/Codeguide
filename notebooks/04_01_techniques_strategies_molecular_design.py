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
    peptides = ["AKLV", "DDWY", "KRFV", "GPGS"]
    rows = []
    for peptide in peptides:
        charge = sum(charged.get(aa, 0) for aa in peptide)
        hydrophobicity = sum(aa in hydrophobic for aa in peptide) / len(peptide)
        score = 0.5 * hydrophobicity + 0.2 * abs(charge) + 0.05 * len(peptide)
        rows.append((peptide, charge, hydrophobicity, score))
    sample_values = [score for *_, score in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {pep} | {charge} | {hydro:.2f} | {score:.2f} |" for pep, charge, hydro, score in rows)
    mo.md(f"""
# Techniques And Strategies In Molecular Design

Short intro: score toy peptides with transparent property rules.

## Learning goals
Relate charge, hydrophobicity, and length to prioritization.

## Background
The peptide properties are simple teaching descriptors.

## Interactive example
| Peptide | Charge | Hydrophobic fraction | Toy score |
| --- | ---: | ---: | ---: |
{table}

## Exercise
Add one acidic and one basic peptide.

## Notes for future editing
Add validated descriptors only when needed.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
