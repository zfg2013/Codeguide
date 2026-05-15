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
    training = [(0.2, 0), (0.4, 0), (0.9, 1), (1.1, 1)]
    neg = statistics.mean(value for value, label in training if label == 0)
    pos = statistics.mean(value for value, label in training if label == 1)
    threshold = (neg + pos) / 2
    candidates = [0.3, 0.6, 0.95]
    rows = [(value, int(value >= threshold)) for value in candidates]
    sample_values = candidates
    example_count = len(candidates)
    example_total = sum(prediction for _, prediction in rows)
    table = "\n".join(f"| {value} | {prediction} |" for value, prediction in rows)
    mo.md(f"""
# Implementing ML Tools And Decisions

Short intro: implement a threshold classifier from scratch.

## Learning goals
Build a simple decision rule without heavyweight packages.

## Background
Training points have one synthetic feature and a binary label.

## Interactive example
Learned threshold: {threshold:.2f}

| Candidate signal | Predicted class |
| ---: | ---: |
{table}

## Exercise
Add a candidate exactly at the threshold.

## Notes for future editing
Add regression from scratch later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
