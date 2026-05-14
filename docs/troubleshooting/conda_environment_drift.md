# Conda Environment Drift

Owner: Computational lead  
Last reviewed: 2026-05-06  
Status: Example troubleshooting entry

## Symptom

A workflow that used to run now fails after package updates, or two people get different results from the same notebook.

## Likely Causes

- The environment was updated without exporting a new file.
- A notebook kernel points to a different environment.
- Packages were installed interactively and never recorded.
- The workflow depends on system tools outside conda.

## Checks

```bash
conda env export --from-history
```

```bash
which python
python -c "import sys; print(sys.executable)"
```

## Fixes

- Recreate the environment from the committed `environment.yml`.
- Record any new package in the environment file.
- Restart the notebook kernel after switching environments.
- Add command-line tool versions to the workflow page.

## Prevention

For stable project environments, prefer a committed `environment.yml` or lock file. Avoid installing packages during a live analysis without recording the change.
