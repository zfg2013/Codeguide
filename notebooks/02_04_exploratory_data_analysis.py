import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import statistics
    import marimo as mo
    return mo, statistics


@app.cell
def _(mo, statistics):
    expression = {"GeneA": [12, 14, 28, 30], "GeneB": [7, 8, 6, 7], "GeneC": [20, 19, 9, 10]}
    samples = ["ctrl_1", "ctrl_2", "treat_1", "treat_2"]
    totals = [sum(values[i] for values in expression.values()) for i in range(len(samples))]
    sample_values = totals
    example_count = len(samples)
    example_total = sum(totals)
    table = "\n".join(f"| {sample} | {total} | {total / example_total:.2f} |" for sample, total in zip(samples, totals))
    means = ", ".join(f"{gene}: {statistics.mean(values):.1f}" for gene, values in expression.items())
    mo.md(f"""
# Exploratory Data Analysis

Short intro: inspect a synthetic expression matrix before modeling.

## Learning goals
Summarize library size and gene-level averages.

## Background
Counts are synthetic values for three genes across four samples.

## Interactive example
| Sample | Total counts | Library share |
| --- | ---: | ---: |
{table}

Gene means: {means}.

## Exercise
Which sample would you inspect first if total counts were low?

## Notes for future editing
Add a small bar chart or PCA-style example.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
