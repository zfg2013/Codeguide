# Codeguide

Codeguide is a static tutorial curriculum for executable marimo WASM notebooks. Each notebook is authored as a marimo `.py` file and exported to `site/marimo/<name>.html` during the GitHub Pages build.

## Start Here

<div class="grid cards" markdown>

- **Statistical Theory**

    Foundations for probability, estimation, uncertainty, and decision-making.

    [Open notebook](marimo/01_statistical_theory.html)

- **Sequencing**

    A practical sequencing workflow from instrument output to validation.

    [Start sequencing module](tutorials/sequencing.md)

- **Machine Learning**

    Exploratory analysis, model decisions, validation, and experiment handoff.

    [Open first ML notebook](marimo/03_01_what_is_machine_learning.html)

- **Molecular Design Engineering**

    Library design, screening, hit QC, and selection for experimentation.

    [Open first design notebook](marimo/04_01_techniques_strategies_molecular_design.html)

</div>

## Publishing Flow

Changes pushed to `main` run the GitHub Actions workflow. The workflow checks the repository structure, builds MkDocs in strict mode, exports every `notebooks/*.py` marimo notebook into `site/marimo/`, and deploys the generated `site/` artifact to GitHub Pages.

## Local Checks

```powershell
py -m unittest discover -s tests
mkdocs build --strict
```
