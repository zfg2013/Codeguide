# Workflow Title

Owner: Name or role  
Last reviewed: YYYY-MM-DD  
Status: Draft, active, deprecated, or example

## Purpose

Describe the scientific or operational question this workflow answers.

## Inputs

| Input | Location | Notes |
| --- | --- | --- |
| Example input | `path/or/system` | Required columns, format, or access notes |

## Environment

List software versions, conda environment files, containers, modules, or system tools.

```bash
command-to-create-or-activate-environment
```

## Steps

1. Step one.
2. Step two.
3. Step three.

```bash
example-command --input path --output path
```

## Outputs

| Output | Location | How to review |
| --- | --- | --- |
| Example output | `path/to/output` | Expected format or QC check |

## Checks

- Check that input sample IDs match metadata.
- Check that output row counts are expected.
- Check logs for warnings or skipped samples.

## Known Limitations

List assumptions, unsupported cases, and places where judgment is required.

## Handoff Notes

Name the project owner, reviewer, and where to find related scripts or notebooks.
