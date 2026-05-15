# Codeguide

Codeguide is a GitHub Pages tutorial curriculum built with MkDocs Material and marimo WASM exports. Markdown pages organize the modules, and marimo `.py` notebooks provide executable browser pages.

## Repository Layout

- `docs/index.md`: wiki-style landing page with marimo notebook cards.
- `docs/tutorials/`: module pages for the executable notebook curriculum.
- `docs/notebooks/`: notebook library linking to exported marimo HTML files.
- `notebooks/`: source marimo `.py` notebooks.
- `.github/workflows/deploy.yml`: GitHub Actions workflow for GitHub Pages.
- `tests/`: structure checks for the tutorial site.

## Local Preview

Install Python 3, then run:

```powershell
py -m pip install -r requirements.txt
mkdocs serve
```

Open the local URL printed by MkDocs, usually `http://127.0.0.1:8000`.

## Editing marimo Notebooks

Create and edit notebooks in the `notebooks/` directory:

```powershell
marimo edit notebooks/01_statistical_theory.py
```

Keep notebooks lightweight enough for browser execution after WASM export.

## WASM Export

Build MkDocs first, then export all source notebooks into `site/marimo/`:

```powershell
mkdocs build --strict
New-Item -ItemType Directory -Force site/marimo
Get-ChildItem notebooks -Filter *.py | ForEach-Object {
  marimo export html-wasm $_.FullName -o "site/marimo/$($_.BaseName).html" --mode run
}
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

The workflow at `.github/workflows/deploy.yml` publishes the MkDocs build to GitHub Pages whenever `main` changes. It builds MkDocs first, then exports every `notebooks/*.py` file with `marimo export html-wasm` into `site/marimo/`, so Markdown links can point at `marimo/<name>.html`.

Repository setup:

1. Open the repository settings on GitHub.
2. Go to Pages.
3. Set the source to GitHub Actions.
4. Push changes to `main`.

The workflow uploads the generated `site/` directory as a Pages artifact and deploys it with `actions/deploy-pages`.

## Adding Notebooks

1. Add a marimo notebook under `notebooks/`.
2. Add a link to `marimo/<name>.html` from `docs/index.md`, `../marimo/<name>.html` from `docs/notebooks/index.md`, or `../../marimo/<name>.html` from tutorial module pages.
3. Add it to `docs/notebooks/index.md`.
4. Add context in the relevant `docs/tutorials/` module page.
5. Run the checks before publishing.
