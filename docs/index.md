# Codeguide

Codeguide is a static tutorial curriculum for executable marimo WASM notebooks. Each notebook is authored as a marimo `.py` file and exported to `site/marimo/<name>.html` during the GitHub Pages build.

## Start Here

<div class="grid cards" markdown>

- **Statistical Theory**

    Foundations for probability, estimation, uncertainty, and decision-making.

    [Start topic module](tutorials/statistical-theory.md)

- **Sequencing**

    A practical sequencing workflow from instrument output to validation.

    [Start topic module](tutorials/sequencing.md)

- **Machine Learning**

    Exploratory analysis, model decisions, validation, and experiment handoff.

    [Start topic module](tutorials/machine-learning.md)

- **Molecular Design & Engineering**

    Library design, screening, hit QC, and selection for experimentation.

    [Start topic module](tutorials/molecular-design-engineering.md)

</div>

## Publishing Flow

Changes pushed to `main` run the GitHub Actions workflow. The workflow checks the repository structure, builds MkDocs in strict mode, exports every `notebooks/*.py` marimo notebook into `site/marimo/`, and deploys the generated `site/` artifact to GitHub Pages.

## Local Checks

```powershell
py -m unittest discover -s tests
mkdocs build --strict
```
