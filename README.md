# Codeguide

Codeguide is a GitHub Pages tutorial site built with MkDocs Material. It is structured as a small wiki: Markdown pages explain concepts, Jupyter notebooks provide runnable examples, and marimo notebooks can be exported as lightweight browser-executable WASM pages.

## Repository Layout

- `docs/index.md`: wiki-style landing page with tutorial cards.
- `docs/tutorials/`: written tutorial pages.
- `docs/notebooks/`: notebook landing page and generated marimo WASM exports.
- `notebooks/`: source notebooks, including `.ipynb` files and marimo `.py` notebooks.
- `.github/workflows/deploy.yml`: GitHub Actions workflow for GitHub Pages.
- `tests/`: structure checks for the tutorial site.

## Local Preview

Install Python 3, then run:

```powershell
py -m pip install -r requirements.txt
mkdocs serve
```

Open the local URL printed by MkDocs, usually `http://127.0.0.1:8000`.

To preview the marimo notebook as a standalone WASM app, export it before serving:

```powershell
marimo export html-wasm notebooks/marimo_example.py -o docs/notebooks/marimo-example --mode run
mkdocs serve
```

## Checks

Run the lightweight repository tests:

```powershell
py -m unittest discover -s tests
```

Run the MkDocs build:

```powershell
mkdocs build --strict
```

## Publishing With GitHub Pages

The workflow at `.github/workflows/deploy.yml` publishes the MkDocs build to GitHub Pages whenever `main` changes. It also exports `notebooks/marimo_example.py` with `marimo export html-wasm` before the MkDocs build, so the static site includes an executable notebook page.

Repository setup:

1. Open the repository settings on GitHub.
2. Go to Pages.
3. Set the source to GitHub Actions.
4. Push changes to `main`.

The workflow uploads the generated `site/` directory as a Pages artifact and deploys it with `actions/deploy-pages`.

## Adding Tutorials

1. Add a Markdown tutorial under `docs/tutorials/`.
2. Add source notebooks under `notebooks/`.
3. Add a Colab badge link for every `.ipynb` notebook on `docs/notebooks/index.md` and any tutorial page that references it.
4. Add the tutorial to `mkdocs.yml` navigation.
5. Run the checks before publishing.

The example notebook Colab URL pattern is:

```text
https://colab.research.google.com/github/zfg2013/Codeguide/blob/main/notebooks/example_python_workflow.ipynb
```
