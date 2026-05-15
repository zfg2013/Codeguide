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
    records = [(2.1, 0), (2.5, 0), (3.8, 1), (4.1, 1), (2.8, 0), (4.4, 1)]
    folds = [records[:2], records[2:4], records[4:]]
    rows = []
    for index, test in enumerate(folds):
        train = [row for fold_id, fold in enumerate(folds) if fold_id != index for row in fold]
        threshold = statistics.mean(score for score, _ in train)
        accuracy = sum((score >= threshold) == bool(label) for score, label in test) / len(test)
        rows.append((index + 1, threshold, accuracy))
    sample_values = [accuracy for _, _, accuracy in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {fold} | {threshold:.2f} | {accuracy:.2f} |" for fold, threshold, accuracy in rows)
    mo.md(f"""
# Cross Validation

Short intro: evaluate a toy threshold classifier on held-out folds.

## Learning goals
Use train/test folds to estimate generalization.

## Background
Synthetic expression scores have binary labels.

## Interactive example
| Fold | Threshold | Accuracy |
| --- | ---: | ---: |
{table}

## Exercise
Change one label and observe which fold is most sensitive.

## Notes for future editing
Add stratified folds later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
