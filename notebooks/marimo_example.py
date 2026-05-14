import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import pandas as pd

    return mo, np, pd


@app.cell
def _(mo):
    mo.md(
        """
        # Example Python Workflow

        This executable notebook computes summary metrics for a small numeric dataset.
        """
    )
    return


@app.cell
def _(np, pd):
    values = np.array([12, 19, 7, 15, 21], dtype=float)
    summary = pd.DataFrame(
        {
            "metric": ["count", "mean", "min", "max"],
            "value": [values.size, values.mean(), values.min(), values.max()],
        }
    )
    return summary, values


@app.cell
def _(summary):
    summary
    return


if __name__ == "__main__":
    app.run()
