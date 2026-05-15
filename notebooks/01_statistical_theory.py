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
    # Statistical Theory

    ## Learning goals
    Placeholder: add goals about probability, uncertainty, estimation, and decisions.

    ## Background
    Placeholder: introduce the statistical ideas learners need before using the example.

    ## Interactive example
    Placeholder: replace the simple summary below with an interactive statistical activity.

    ## Exercise
    Placeholder: ask learners to modify the assumptions and interpret the result.

    ## Notes for future editing
    Placeholder: add references, diagrams, and domain-specific datasets.
    """)
    return


@app.cell
def _():
    sample_values = [2, 4, 6, 8]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    example_mean = example_total / example_count
    {"count": example_count, "total": example_total, "mean": example_mean}
    return example_count, example_mean, example_total, sample_values


if __name__ == "__main__":
    app.run()
