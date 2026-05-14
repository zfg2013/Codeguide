# Notebooks

Source notebooks live in the repository-level `notebooks/` directory as marimo `.py` files. The GitHub Pages workflow exports each notebook to static WASM HTML under this section.

## marimo Notebooks

| Source notebook | WASM export |
| --- | --- |
| [`notebooks/marimo_example.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/marimo_example.py) | [Open exported notebook](marimo-example/) |

Add new notebooks as `notebooks/<name>.py`. The deployment workflow converts underscores to hyphens for the exported directory, so `notebooks/my_notebook.py` is published at `docs/notebooks/my-notebook/`.
