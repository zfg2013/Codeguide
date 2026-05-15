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
    # Sequence Alignment

    ## Learning goals
    Placeholder: explain alignment, mapping rate, and reference choice.

    ## Background
    Placeholder: introduce reads, reference genomes, indexes, and aligner outputs.

    ## Interactive example
    Placeholder: summarize alignment metrics for a small batch.

    ## Exercise
    Placeholder: ask learners to flag low-quality samples.

    ## Notes for future editing
    Placeholder: add aligner-specific parameters and QC plots.
    """)
    return


@app.cell
def _():
    sample_values = [94, 88, 91]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    example_mean = example_total / example_count
    {"samples": example_count, "mean_mapping_rate": example_mean}
    return example_count, example_mean, example_total, sample_values


if __name__ == "__main__":
    app.run()
