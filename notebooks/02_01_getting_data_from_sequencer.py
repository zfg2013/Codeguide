import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import statistics
    import marimo as mo
    return mo, statistics


@app.cell
def _(mo, statistics):
    reads = [("read_001", "ACGTACGT", "IIIIIIII"), ("read_002", "ACGTNNGT", "III!!III"), ("read_003", "TTAACCGG", "HHHHHHHH")]
    rows = []
    for name, sequence, quality in reads:
        scores = [ord(char) - 33 for char in quality]
        rows.append((name, len(sequence), sequence.count("N"), round(statistics.mean(scores), 1)))
    sample_values = [row[1] for row in rows]
    example_count = len(rows)
    example_total = sum(sample_values)
    table = "\n".join(f"| {name} | {length} | {n_bases} | {mean_q} |" for name, length, n_bases, mean_q in rows)
    mo.md(f"""
# Getting Data From Sequencer

Short intro: summarize mock FASTQ reads before downstream analysis.

## Learning goals
Inspect read length, ambiguous bases, and quality scores.

## Background
The data are synthetic FASTQ-like records.

## Interactive example
| Read | Length | N bases | Mean quality |
| --- | ---: | ---: | ---: |
{table}

## Exercise
Flag reads with an `N` base or mean quality below 35.

## Notes for future editing
Add sample-sheet and lane summaries.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
