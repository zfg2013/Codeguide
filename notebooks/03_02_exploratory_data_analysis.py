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
    features = {"signal": [0.2, 0.3, 0.8, 0.9, 1.1], "noise": [4.2, 4.0, 4.1, 8.5, 4.3], "batch": [1, 1, 2, 2, 2]}
    rows = [(name, min(values), max(values), statistics.mean(values)) for name, values in features.items()]
    sample_values = features["signal"]
    example_count = len(sample_values)
    example_total = sum(sample_values)
    table = "\n".join(f"| {name} | {low} | {high} | {mean:.2f} |" for name, low, high, mean in rows)
    mo.md(f"""
# Exploratory Data Analysis

Short intro: inspect synthetic feature ranges before modeling.

## Learning goals
Summarize features and spot questionable values.

## Background
The table is a small synthetic ML feature set.

## Interactive example
| Feature | Min | Max | Mean |
| --- | ---: | ---: | ---: |
{table}

## Exercise
Which feature has an outlier-like value?

## Notes for future editing
Add feature-pair summaries later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
