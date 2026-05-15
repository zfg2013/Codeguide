import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    mo.md("""
    # Enrichment Analysis

    ## Learning goals
    Placeholder: explain gene sets, background universes, and enrichment evidence.

    ## Background
    Placeholder: introduce pathway databases and overrepresentation concepts.

    ## Interactive example
    Placeholder: compute a simple overlap fraction.

    ## Exercise
    Placeholder: ask learners to choose an appropriate background set.

    ## Notes for future editing
    Placeholder: add pathway examples, ranking methods, and interpretation caveats.
    """)
    return


@app.cell
def _():
    sample_values = [1, 1, 0, 1, 0]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"gene_set_size": example_count, "overlap_count": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
