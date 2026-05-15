# Tutorials

Codeguide tutorials are organized as executable marimo WASM modules. Each module page lists editable source notebooks and links to the exported HTML pages generated during deployment.

## Modules

- [Statistical Theory](statistical-theory.md): probability, uncertainty, inference, and decision-making.
- [Sequencing](sequencing.md): a sequencing data workflow from instrument output through validation.
- [Machine Learning](machine-learning.md): data exploration, model decisions, validation, and experiment handoff.
- [Molecular Design Engineering](molecular-design-engineering.md): molecular library design, screening, QC, and hit selection.

## Add A Tutorial

1. Add a marimo notebook under `notebooks/`.
2. Link its exported `../../marimo/<name>.html` page from the relevant tutorial module.
3. Add it to the notebook library.
4. Run the tests and strict MkDocs build before publishing.
