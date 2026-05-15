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
    # What Is Machine Learning

    ## Learning goals
    Placeholder: explain features, labels, predictions, and evaluation.

    ## Background
    Placeholder: distinguish modeling goals from statistical description.

    ## Interactive example
    Placeholder: compute a simple baseline prediction.

    ## Exercise
    Placeholder: ask learners to define inputs, outputs, and success criteria.

    ## Notes for future editing
    Placeholder: add examples from classification, regression, and ranking.
    """)
    return


@app.cell
def _():
    sample_values = [0, 1, 1, 0, 1]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"examples": example_count, "positive_labels": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
