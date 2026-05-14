# RNA-seq Differential Expression

Owner: Computational lead  
Last reviewed: 2026-05-06  
Status: Example workflow

## Purpose

Compare gene expression between treated and control samples after alignment and quantification have completed.

## Inputs

| Input | Location | Notes |
| --- | --- | --- |
| Count matrix | `shared/projects/example_rnaseq/counts/gene_counts.tsv` | Raw integer counts by gene and sample |
| Sample metadata | `shared/projects/example_rnaseq/metadata/sample_sheet.tsv` | Must contain `sample_id`, `condition`, and `batch` |
| Gene annotation | `shared/references/gencode/v44/gene_annotation.tsv` | Stable reference version for this project |

## Environment

Use the project environment file:

```bash
conda env create -f envs/rnaseq-deseq2.yml
conda activate rnaseq-deseq2
```

## Steps

1. Confirm sample IDs match between the count matrix and metadata.
2. Run the differential expression script.
3. Review PCA and sample distance plots for outliers.
4. Export normalized counts, model results, and a short QC summary.

```bash
Rscript scripts/run_deseq2.R \
  --counts shared/projects/example_rnaseq/counts/gene_counts.tsv \
  --metadata shared/projects/example_rnaseq/metadata/sample_sheet.tsv \
  --design "~ batch + condition" \
  --out results/deseq2_2026_05_06
```

## Outputs

| Output | Meaning |
| --- | --- |
| `deseq2_results.tsv` | Wald test results with log2 fold change and adjusted p value |
| `normalized_counts.tsv` | Size-factor normalized counts |
| `qc_plots.pdf` | PCA, library size, dispersion, and sample distance plots |
| `run_summary.md` | Human-readable notes from the run |

## Checks

- No sample IDs are dropped during metadata matching.
- PCA does not show obvious sample swaps.
- Adjusted p values are present and not all missing.
- The output directory contains the command log.

## Known Limitations

This workflow assumes bulk RNA-seq counts. It is not appropriate for single-cell data or transcript-level differential usage without modification.
