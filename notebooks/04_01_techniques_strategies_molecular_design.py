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
    # Techniques Strategies Molecular Design

    ## Learning goals
    Placeholder: compare design strategies for molecular optimization.

    ## Background
    Placeholder: introduce library diversity, constraints, and scoring.

    ## Interactive example
    Placeholder: summarize a simple set of strategy scores.

    ## Exercise
    Placeholder: ask learners to choose a strategy for a constrained campaign.

    ## Notes for future editing
    Placeholder: add docking, generative, and medicinal chemistry examples.
    """)
    return


@app.cell
def _():
    sample_values = [3, 5, 4]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"strategies": example_count, "combined_score": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
