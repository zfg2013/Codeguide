import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    from collections import Counter
    import marimo as mo
    return Counter, mo


@app.cell
def _(Counter, mo):
    annotations = {"read_001": "GeneA", "read_002": "GeneB", "read_003": "GeneA", "read_004": "GeneC"}
    mapped_reads = ["read_001", "read_002", "read_003", "read_005", "read_004", "read_003"]
    counts = Counter(annotations.get(read, "unassigned") for read in mapped_reads)
    sample_values = list(counts.values())
    example_count = len(mapped_reads)
    example_total = sum(count for gene, count in counts.items() if gene != "unassigned")
    table = "\n".join(f"| {gene} | {count} |" for gene, count in sorted(counts.items()))
    mo.md(f"""
# Counting Mapped Annotated Reads

Short intro: convert mapped read IDs into a gene-count table.

## Learning goals
Connect read assignment to gene counts.

## Background
A small annotation dictionary maps reads to genes.

## Interactive example
| Gene | Count |
| --- | ---: |
{table}

## Exercise
Add an annotation for `read_005` and rerun the table.

## Notes for future editing
Add strandedness and multimapping examples.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
