import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    reference = "ACGTACGTGACCTTACGT"
    reads = ["ACGT", "GACC", "TTAC", "GGGG", "TACG"]
    alignments = [(read, reference.find(read)) for read in reads]
    sample_values = [1 if start >= 0 else 0 for _, start in alignments]
    example_count = len(reads)
    example_total = sum(sample_values)
    table = "\n".join(f"| {read} | {'mapped' if start >= 0 else 'unmapped'} | {start if start >= 0 else '-'} |" for read, start in alignments)
    mo.md(f"""
# Sequence Alignment

Short intro: map toy reads to a tiny reference with exact string matching.

## Learning goals
Explain mapped and unmapped reads.

## Background
This is a teaching simplification, not a production aligner.

## Interactive example
Reference: `{reference}`

| Read | Status | Start |
| --- | --- | ---: |
{table}

## Exercise
Add a read with one mismatch and predict whether it maps.

## Notes for future editing
Add mismatch counts and seed matching.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
