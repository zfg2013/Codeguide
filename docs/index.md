# Codeguide

Codeguide is a static tutorial wiki for executable marimo WASM notebooks. Each notebook is authored as a marimo `.py` file and exported to browser-runnable HTML during the GitHub Pages build.

## Start Here

<div class="grid cards" markdown>

- **Executable Notebook**

    Open the sample marimo WASM notebook as a static browser page generated from the source notebook.

    [Open notebook](notebooks/marimo-example/)

- **Notebook Library**

    Browse source notebooks and their exported static WASM pages.

    [Browse notebooks](notebooks/index.md)

- **Tutorial Index**

    See how to add new marimo notebooks to the wiki and deployment workflow.

    [View tutorials](tutorials/index.md)

</div>

## Publishing Flow

Changes pushed to `main` run the GitHub Actions workflow. The workflow checks the repository structure, exports every `notebooks/*.py` marimo notebook to a WASM page, builds MkDocs in strict mode, and deploys the generated `site/` artifact to GitHub Pages.

## Local Checks

```powershell
py -m unittest discover -s tests
mkdocs build --strict
```
