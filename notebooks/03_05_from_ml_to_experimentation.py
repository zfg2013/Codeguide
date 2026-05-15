import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return mo


@app.cell
def _(mo):
    candidates = [("A", 0.92, 0.20, 2), ("B", 0.81, 0.70, 3), ("C", 0.66, 0.90, 1), ("D", 0.74, 0.40, 2)]
    ranked = sorted(((name, score, novelty, cost, 0.6 * score + 0.3 * novelty - 0.05 * cost) for name, score, novelty, cost in candidates), key=lambda row: row[4], reverse=True)
    sample_values = [priority for *_, priority in ranked]
    example_count = len(ranked)
    example_total = sum(sample_values)
    table = "\n".join(f"| {name} | {score} | {novelty} | {cost} | {priority:.3f} |" for name, score, novelty, cost, priority in ranked)
    mo.md(f"""
# From ML To Experimentation

Short intro: turn model scores into an experimental priority list.

## Learning goals
Balance confidence, novelty, and cost.

## Background
Candidates and scores are synthetic.

## Interactive example
| Candidate | Model score | Novelty | Cost | Priority |
| --- | ---: | ---: | ---: | ---: |
{table}

## Exercise
Increase the cost penalty and rerank.

## Notes for future editing
Add uncertainty and replicate planning.
""")
    return example_count, example_total, sample_values


if __name__ == "__main__":
    app.run()
