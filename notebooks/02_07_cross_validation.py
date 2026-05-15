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
    # Sequencing Cross Validation

    ## Learning goals
    Placeholder: validate findings across datasets, methods, or held-out samples.

    ## Background
    Placeholder: introduce replication, sensitivity analysis, and robustness.

    ## Interactive example
    Placeholder: compare agreement across simple validation flags.

    ## Exercise
    Placeholder: ask learners to define validation criteria before looking at results.

    ## Notes for future editing
    Placeholder: add external cohort and method-comparison examples.
    """)
    return


@app.cell
def _():
    sample_values = [True, True, False, True]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"checks": example_count, "validated": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
