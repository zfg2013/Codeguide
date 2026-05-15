import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    mo.md("""
    # Getting Data From Sequencer

    ## Learning goals
    Placeholder: describe how raw run outputs become analysis-ready inputs.

    ## Background
    Placeholder: define run folders, sample sheets, FASTQ files, and metadata.

    ## Interactive example
    Placeholder: inspect a small manifest of sequencing files.

    ## Exercise
    Placeholder: ask learners to identify missing metadata and naming issues.

    ## Notes for future editing
    Placeholder: add platform-specific examples and handoff checklists.
    """)
    return


@app.cell
def _():
    sample_values = [12, 10, 11]
    example_total = sum(sample_values)
    example_count = len(sample_values)
    {"files": example_count, "total_gb": example_total}
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
