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
    # Sequencing Exploratory Data Analysis

    ## Learning goals
    Placeholder: identify structure, outliers, and batch effects in count data.

    ## Background
    Placeholder: introduce normalization, sample distance, and exploratory plots.

    ## Interactive example
    Placeholder: summarize sample-level library sizes.

    ## Exercise
    Placeholder: ask learners to choose samples for follow-up review.

    ## Notes for future editing
    Placeholder: add PCA, heatmaps, and metadata-driven filtering.
    """)
    return


@app.cell
def _():
    sample_values = [3.2, 3.8, 2.9, 4.1]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    example_mean = example_total / example_count
    {"samples": example_count, "mean_library_size_millions": round(example_mean, 2)}
    return example_count, example_mean, example_total, sample_values


if __name__ == "__main__":
    app.run()
