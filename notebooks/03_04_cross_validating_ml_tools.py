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
    # Cross Validating ML Tools

    ## Learning goals
    Placeholder: explain folds, held-out data, and validation metrics.

    ## Background
    Placeholder: introduce why validation estimates future performance.

    ## Interactive example
    Placeholder: summarize scores across simple folds.

    ## Exercise
    Placeholder: ask learners to compare average and worst-fold performance.

    ## Notes for future editing
    Placeholder: add stratification, leakage checks, and confidence intervals.
    """)
    return


@app.cell
def _():
    sample_values = [0.72, 0.81, 0.77]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    example_mean = example_total / example_count
    {"folds": example_count, "mean_score": round(example_mean, 3)}
    return example_count, example_mean, example_total, sample_values


if __name__ == "__main__":
    app.run()
