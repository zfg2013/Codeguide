import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    candidates = [("AKLV", 7, True, 0.4), ("GPGS", 4, True, 0.8), ("AVAV", 5, False, 0.5), ("KRFV", 8, True, 0.3)]
    ranked = sorted(((pep, screen, qc, novelty, screen / 10 + 0.3 * novelty + (0.2 if qc else -0.5)) for pep, screen, qc, novelty in candidates), key=lambda row: row[4], reverse=True)
    selected = [pep for pep, _, qc, _, _ in ranked if qc][:2]
    sample_values = [score for *_, score in ranked]
    example_count = len(ranked)
    example_total = sum(sample_values)
    table = "\n".join(f"| {pep} | {screen} | {qc} | {novelty} | {score:.2f} |" for pep, screen, qc, novelty, score in ranked)
    mo.md(f"""
# Hit Selection For Experimentation

Short intro: rank QC-passing peptide hits for experimental testing.

## Learning goals
Balance screen score, QC status, and novelty.

## Background
Candidates are synthetic and scores are teaching-only.

## Interactive example
| Peptide | Screen | Pass QC | Novelty | Selection score |
| --- | ---: | --- | ---: | ---: |
{table}

Selected for the next experiment: {', '.join(selected)}.

## Exercise
Increase the novelty weight and rerank.

## Notes for future editing
Add budget constraints and replicate counts later.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
