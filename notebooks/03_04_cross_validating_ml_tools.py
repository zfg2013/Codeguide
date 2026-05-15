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
    data = [(0.1, 0), (0.4, 0), (0.6, 0), (0.9, 1), (1.2, 1), (1.5, 1)]
    folds = [data[0:2], data[2:4], data[4:6]]
    rows = []
    for i, test in enumerate(folds):
        train = [row for j, fold in enumerate(folds) if j != i for row in fold]
        neg = statistics.mean(value for value, label in train if label == 0)
        pos = statistics.mean(value for value, label in train if label == 1)
        threshold = (neg + pos) / 2
        accuracy = sum((value >= threshold) == bool(label) for value, label in test) / len(test)
        rows.append((i + 1, threshold, accuracy))
    sample_values = [accuracy for _, _, accuracy in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {fold} | {threshold:.2f} | {accuracy:.2f} |" for fold, threshold, accuracy in rows)
    mo.md(f"""
# Cross Validating ML Tools

Short intro: manually run k-fold validation.

## Learning goals
Compare fold-level model performance.

## Background
The data are synthetic ordered samples.

## Interactive example
| Fold | Learned threshold | Accuracy |
| --- | ---: | ---: |
{table}

## Exercise
Shuffle fold membership and compare results.

## Notes for future editing
Add repeated folds later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
