import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import math
    import statistics
    import marimo as mo
    return math, mo, statistics


@app.cell
def _(math, mo, statistics):
    counts = {"GeneA": ([12, 14, 13], [28, 31, 29]), "GeneB": ([8, 7, 9], [7, 8, 8]), "GeneC": ([20, 18, 19], [10, 11, 9])}
    rows = []
    for gene, (control, treated) in counts.items():
        c_mean = statistics.mean(control)
        t_mean = statistics.mean(treated)
        pooled = math.sqrt(statistics.variance(control) / 3 + statistics.variance(treated) / 3)
        rows.append((gene, t_mean / c_mean, (t_mean - c_mean) / pooled))
    sample_values = [abs(t_stat) for _, _, t_stat in rows]
    example_count = len(rows)
    example_total = sum(value > 2 for value in sample_values)
    table = "\n".join(f"| {gene} | {fc:.2f} | {t_stat:.2f} |" for gene, fc, t_stat in rows)
    mo.md(f"""
# Differential Analysis

Short intro: compare synthetic control and treatment counts.

## Learning goals
Use fold change and a toy t-statistic.

## Background
This is a teaching summary, not a production differential-expression model.

## Interactive example
| Gene | Fold change | Toy t-statistic |
| --- | ---: | ---: |
{table}

## Exercise
Change GeneB treatment counts to create a stronger effect.

## Notes for future editing
Add multiple-testing intuition later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
