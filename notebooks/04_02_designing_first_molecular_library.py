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
    # Designing First Molecular Library

    ## Learning goals
    Placeholder: define first-pass molecular library design criteria.

    ## Background
    Placeholder: introduce diversity, synthesizability, and target hypotheses.

    ## Interactive example
    Placeholder: count molecules passing simple design criteria.

    ## Exercise
    Placeholder: ask learners to revise criteria under a budget constraint.

    ## Notes for future editing
    Placeholder: add scaffold, property, and vendor-availability examples.
    """)
    return


@app.cell
def _():
    sample_values = [True, False, True, True]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"library_candidates": example_count, "selected": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
