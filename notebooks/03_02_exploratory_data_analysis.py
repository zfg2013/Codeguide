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
    # Machine Learning Exploratory Data Analysis

    ## Learning goals
    Placeholder: inspect distributions, missingness, leakage, and feature quality.

    ## Background
    Placeholder: explain how EDA shapes modeling decisions.

    ## Interactive example
    Placeholder: summarize simple feature values.

    ## Exercise
    Placeholder: ask learners to identify a risky feature.

    ## Notes for future editing
    Placeholder: add visualization and leakage examples.
    """)
    return


@app.cell
def _():
    sample_values = [5, 7, 7, 10]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    example_mean = example_total / example_count
    {"rows": example_count, "mean_feature_value": example_mean}
    return example_count, example_mean, example_total, sample_values


if __name__ == "__main__":
    app.run()
