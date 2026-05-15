import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    library = ["AKL", "ADL", "GKV", "GDV", "AKV", "ADV"]
    hydrophobic = set("AILMFWV")
    rows = []
    for peptide in library:
        positive = peptide.count("K") + peptide.count("R")
        hydrophobic_count = sum(aa in hydrophobic for aa in peptide)
        score = 2 * positive + hydrophobic_count
        rows.append((peptide, positive, hydrophobic_count, score))
    rows = sorted(rows, key=lambda row: row[3], reverse=True)
    sample_values = [score for *_, score in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {pep} | {positive} | {hydro} | {score} |" for pep, positive, hydro, score in rows)
    mo.md(f"""
# Screening A First Molecular Library

Short intro: screen a toy peptide library with a simple score.

## Learning goals
Rank candidates by transparent screening criteria.

## Background
The scoring rule rewards positive charge and hydrophobic residues.

## Interactive example
| Peptide | Positive charge | Hydrophobic count | Screen score |
| --- | ---: | ---: | ---: |
{table}

## Exercise
Penalize hydrophobic count above 2.

## Notes for future editing
Add assay noise and replicates later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
