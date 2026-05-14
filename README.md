# Codeguide

Codeguide is a GitHub Pages tutorial site built with MkDocs Material and marimo WASM exports. It is structured as a small wiki: Markdown pages organize the catalog, and marimo `.py` notebooks provide the executable browser pages.

## Repository Layout

- `docs/index.md`: wiki-style landing page with marimo notebook cards.
- `docs/tutorials/`: short tutorial index pages for executable notebooks.
- `docs/notebooks/`: notebook landing page and generated marimo WASM exports.
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
marimo edit notebooks/marimo_example.py
```

Keep notebooks lightweight enough for browser execution after WASM export.

## WASM Export

Export all source notebooks into `docs/notebooks/` before a local strict build:

```powershell
Get-ChildItem notebooks -Filter *.py | ForEach-Object {
  $name = $_.BaseName.Replace("_", "-")
  marimo export html-wasm $_.FullName -o "docs/notebooks/$name" --mode run
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

The workflow at `.github/workflows/deploy.yml` publishes the MkDocs build to GitHub Pages whenever `main` changes. It exports every `notebooks/*.py` file with `marimo export html-wasm` before the MkDocs build, so the static site includes executable notebook pages.

Repository setup:

1. Open the repository settings on GitHub.
2. Go to Pages.
3. Set the source to GitHub Actions.
4. Push changes to `main`.

The workflow uploads the generated `site/` directory as a Pages artifact and deploys it with `actions/deploy-pages`.

## Adding Notebooks

1. Add a marimo notebook under `notebooks/`.
2. Add a link to its exported page in `docs/notebooks/index.md`.
3. Add a short tutorial entry in `docs/tutorials/index.md` if the notebook needs context.
4. Run the checks before publishing.
