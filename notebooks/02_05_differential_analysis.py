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
    # Differential Analysis

    ## Learning goals
    Placeholder: explain contrasts, effect sizes, uncertainty, and multiple testing.

    ## Background
    Placeholder: introduce model design and differential signal interpretation.

    ## Interactive example
    Placeholder: classify simple fold-change values.

    ## Exercise
    Placeholder: ask learners to separate statistical and practical significance.

    ## Notes for future editing
    Placeholder: add model formulas, covariates, and result-table examples.
    """)
    return


@app.cell
def _():
    sample_values = [1.2, -0.4, 2.1, 0.0]
    example_total = sum(value > 1 for value in sample_values)
    example_count = len(sample_values)
    {"tested_features": example_count, "large_effects": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
