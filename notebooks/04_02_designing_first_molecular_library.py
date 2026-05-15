import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    from itertools import product
    import marimo as mo
    return mo, product


@app.cell
def _(mo, product):
    positions = [["A", "G"], ["K", "D"], ["L", "V"]]
    library = ["".join(peptide) for peptide in product(*positions)]
    sample_values = [len(peptide) for peptide in library]
    example_count = len(library)
    example_total = sum(sample_values)
    table = "\n".join(f"| {index} | {peptide} | {len(peptide)} |" for index, peptide in enumerate(library, 1))
    mo.md(f"""
# Designing A First Molecular Library

Short intro: generate a tiny combinatorial peptide library.

## Learning goals
Understand position-wise library enumeration.

## Background
Allowed residues are synthetic design choices.

## Interactive example
| Design | Peptide | Length |
| ---: | --- | ---: |
{table}

## Exercise
Add a third residue at position 1 and recalculate size.

## Notes for future editing
Add synthesis-exclusion rules later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
