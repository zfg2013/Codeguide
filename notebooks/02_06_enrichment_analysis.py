import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    universe = {"GeneA", "GeneB", "GeneC", "GeneD", "GeneE", "GeneF", "GeneG", "GeneH"}
    hits = {"GeneA", "GeneC", "GeneD"}
    pathways = {"stress_response": {"GeneA", "GeneC", "GeneE"}, "cell_cycle": {"GeneB", "GeneD", "GeneF"}, "metabolism": {"GeneG", "GeneH"}}
    rows = []
    for name, genes in pathways.items():
        overlap = len(hits & genes)
        expected = len(hits) * len(genes) / len(universe)
        rows.append((name, overlap, expected))
    sample_values = [overlap for _, overlap, _ in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {name} | {overlap} | {expected:.2f} |" for name, overlap, expected in rows)
    mo.md(f"""
# Enrichment Analysis

Short intro: compare hit-gene overlap with simple expectations.

## Learning goals
Build intuition for gene-set enrichment.

## Background
The universe, hits, and pathways are synthetic.

## Interactive example
| Pathway | Overlap | Expected overlap |
| --- | ---: | ---: |
{table}

## Exercise
Add `GeneE` to the hit list and rerun the overlap table.

## Notes for future editing
Add a permutation demo later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
