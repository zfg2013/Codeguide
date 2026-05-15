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
    samples = [("A", 1.2, "low"), ("B", 1.4, "low"), ("C", 3.9, "high"), ("D", 4.2, "high")]
    threshold = statistics.mean(feature for _, feature, _ in samples)
    rows = [(name, label, "above_mean" if feature >= threshold else "below_mean") for name, feature, label in samples]
    sample_values = [feature for _, feature, _ in samples]
    example_count = len(samples)
    example_total = sum(sample_values)
    table = "\n".join(f"| {name} | {label} | {group} |" for name, label, group in rows)
    mo.md(f"""
# What Is Machine Learning?

Short intro: contrast supervised labels with an unsupervised grouping rule.

## Learning goals
Distinguish labels from learned or discovered groups.

## Background
The table uses one synthetic feature.

## Interactive example
| Sample | Supervised label | Unsupervised group |
| --- | --- | --- |
{table}

## Exercise
Add a fifth sample between the clusters.

## Notes for future editing
Add two-feature plots later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
