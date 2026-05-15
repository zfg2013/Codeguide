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
    # Hit Selection For Experimentation

    ## Learning goals
    Placeholder: prioritize hits for experimental validation.

    ## Background
    Placeholder: introduce balancing potency, novelty, feasibility, and risk.

    ## Interactive example
    Placeholder: rank a simple set of hit scores.

    ## Exercise
    Placeholder: ask learners to justify a final experimental shortlist.

    ## Notes for future editing
    Placeholder: add decision matrices and experiment-request templates.
    """)
    return


@app.cell
def _():
    sample_values = [6, 9, 7, 4]
    example_total = sum(score >= 7 for score in sample_values)
    example_count = len(sample_values)
    {"candidate_hits": example_count, "selected_for_experiment": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
