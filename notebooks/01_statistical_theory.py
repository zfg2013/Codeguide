import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import math
    import marimo as mo
    return math, mo


@app.cell
def _(math, mo):
    sample_values = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
    example_count = len(sample_values)
    example_total = sum(sample_values)
    p_hat = example_total / example_count
    se = math.sqrt(p_hat * (1 - p_hat) / example_count)
    ci = (p_hat - 1.96 * se, p_hat + 1.96 * se)
    z = (p_hat - 0.5) / se
    p_value = 2 * (1 - 0.5 * (1 + math.erf(abs(z) / math.sqrt(2))))
    mo.md(f"""
# Statistical Theory

Short intro: estimate uncertainty from a tiny synthetic Bernoulli sample.

## Learning goals
Understand sampling, confidence intervals, and a toy p-value.

## Background
Each value is a synthetic success or failure.

## Interactive example
| Quantity | Value |
| --- | ---: |
| Successes | {example_total} |
| Trials | {example_count} |
| Probability estimate | {p_hat:.2f} |
| 95 percent CI | ({ci[0]:.2f}, {ci[1]:.2f}) |
| Approximate p-value vs 0.50 | {p_value:.3f} |

## Exercise
Change two successes to failures and rerun the summary.

## Notes for future editing
Add sliders for sample size and true probability.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
