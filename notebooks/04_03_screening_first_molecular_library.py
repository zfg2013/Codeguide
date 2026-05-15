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
    # Screening First Molecular Library

    ## Learning goals
    Placeholder: explain screening readouts, controls, and primary hit calls.

    ## Background
    Placeholder: introduce assay windows, replicate behavior, and noise.

    ## Interactive example
    Placeholder: count simple hits above an activity threshold.

    ## Exercise
    Placeholder: ask learners to choose a screening threshold.

    ## Notes for future editing
    Placeholder: add plate layout, controls, and normalization examples.
    """)
    return


@app.cell
def _():
    sample_values = [0.1, 0.8, 0.6, 0.2]
    example_total = sum(activity >= 0.5 for activity in sample_values)
    example_count = len(sample_values)
    {"screened": example_count, "primary_hits": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
