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
    # From ML To Experimentation

    ## Learning goals
    Placeholder: translate model outputs into experimental priorities.

    ## Background
    Placeholder: introduce uncertainty, feasibility, and resource constraints.

    ## Interactive example
    Placeholder: count candidates above a simple priority threshold.

    ## Exercise
    Placeholder: ask learners to justify a shortlist for experimentation.

    ## Notes for future editing
    Placeholder: add assay constraints and decision-review templates.
    """)
    return


@app.cell
def _():
    sample_values = [0.9, 0.3, 0.75, 0.55]
    example_total = sum(score >= 0.7 for score in sample_values)
    example_count = len(sample_values)
    {"candidates": example_count, "experiment_ready": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
