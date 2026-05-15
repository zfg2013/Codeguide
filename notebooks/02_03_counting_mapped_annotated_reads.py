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
    # Counting Mapped Annotated Reads

    ## Learning goals
    Placeholder: explain how aligned reads become feature counts.

    ## Background
    Placeholder: introduce annotations, genomic features, and count matrices.

    ## Interactive example
    Placeholder: compute basic count totals across features.

    ## Exercise
    Placeholder: ask learners to compare counts across samples.

    ## Notes for future editing
    Placeholder: add strandedness, multimapping, and annotation-version examples.
    """)
    return


@app.cell
def _():
    sample_values = [1200, 1500, 900]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"features": example_count, "total_counts": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
