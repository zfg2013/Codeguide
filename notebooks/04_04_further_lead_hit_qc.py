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
    # Further Lead Hit QC

    ## Learning goals
    Placeholder: evaluate hits for quality, robustness, and follow-up feasibility.

    ## Background
    Placeholder: introduce counter-screens, artifacts, and confirmatory assays.

    ## Interactive example
    Placeholder: summarize simple QC pass flags.

    ## Exercise
    Placeholder: ask learners to remove problematic hits before selection.

    ## Notes for future editing
    Placeholder: add PAINS, aggregation, and assay-interference examples.
    """)
    return


@app.cell
def _():
    sample_values = [True, True, False, True, False]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"hits_reviewed": example_count, "qc_pass": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
