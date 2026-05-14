# Example Python Workflow

This tutorial shows the expected shape of a Codeguide page: a short objective, reproducible steps, and links to runnable notebooks.

## Notebook Versions

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/zfg2013/Codeguide/blob/main/notebooks/example_python_workflow.ipynb)

- Jupyter notebook source: [`notebooks/example_python_workflow.ipynb`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/example_python_workflow.ipynb)
- marimo source notebook: [`notebooks/marimo_example.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/marimo_example.py)
- marimo WASM page: [Open the executable notebook](../notebooks/marimo-example/)

## Goal

Given a small list of observations, compute the total, mean, minimum, and maximum in a simple vectorized style.

## Steps

1. Load the observations.
2. Convert values to a numeric array.
3. Compute summary metrics.
4. Present the result as a compact table.

```python
import numpy as np
import pandas as pd

values = np.array([12, 19, 7, 15, 21], dtype=float)
summary = pd.DataFrame(
    {
        "metric": ["count", "mean", "min", "max"],
        "value": [values.size, values.mean(), values.min(), values.max()],
    }
)
summary
```

## Expected Output

| metric | value |
| --- | ---: |
| count | 5.0 |
| mean | 14.8 |
| min | 7.0 |
| max | 21.0 |

## Checks

Before publishing updates, run:

```powershell
py -m unittest discover -s tests
mkdocs build --strict
```
