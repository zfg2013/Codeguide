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
    # Implementing ML Tools And Decisions

    ## Learning goals
    Placeholder: connect modeling tools to explicit decisions and constraints.

    ## Background
    Placeholder: introduce baselines, thresholds, and model selection.

    ## Interactive example
    Placeholder: apply a simple decision threshold.

    ## Exercise
    Placeholder: ask learners to vary the threshold and inspect tradeoffs.

    ## Notes for future editing
    Placeholder: add model cards, decision tables, and uncertainty notes.
    """)
    return


@app.cell
def _():
    sample_values = [0.2, 0.8, 0.6, 0.4]
    example_total = sum(score >= 0.5 for score in sample_values)
    example_count = len(sample_values)
    {"predictions": example_count, "selected": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
