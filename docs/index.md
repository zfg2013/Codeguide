# Codeguide

Codeguide is a static tutorial wiki for practical programming notes, reproducible walkthroughs, and lightweight executable notebooks.

## Start Here

<div class="grid cards" markdown>

- **Example Python Workflow**

    Load a small dataset, compute summary metrics with vectorized Python, and compare the Markdown, Jupyter, and marimo versions.

    [Open tutorial](tutorials/example-python-workflow.md)

- **Notebook Library**

    Launch Jupyter notebooks in Colab or open browser-executable marimo notebooks exported during the Pages build.

    [Browse notebooks](notebooks/index.md)

- **Tutorial Index**

    See all written guides and use the existing structure as the template for new tutorial pages.

    [View tutorials](tutorials/index.md)

</div>

## Publishing Flow

Changes pushed to `main` run the GitHub Actions workflow. The workflow checks the repository structure, exports the marimo notebook to a WASM page, builds MkDocs in strict mode, and deploys the generated `site/` artifact to GitHub Pages.

## Local Checks

```powershell
py -m unittest discover -s tests
mkdocs build --strict
```
