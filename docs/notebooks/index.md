# Notebooks

Source notebooks live in the repository-level `notebooks/` directory as marimo `.py` files. The GitHub Pages workflow exports each notebook to static WASM HTML at `site/marimo/<name>.html`.

## Statistical Theory

| Source notebook | WASM export |
| --- | --- |
| [`01_statistical_theory.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/01_statistical_theory.py) | [Open](../marimo/01_statistical_theory.html) |

## Sequencing

| Source notebook | WASM export |
| --- | --- |
| [`02_01_getting_data_from_sequencer.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_01_getting_data_from_sequencer.py) | [Open](../marimo/02_01_getting_data_from_sequencer.html) |
| [`02_02_sequence_alignment.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_02_sequence_alignment.py) | [Open](../marimo/02_02_sequence_alignment.html) |
| [`02_03_counting_mapped_annotated_reads.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_03_counting_mapped_annotated_reads.py) | [Open](../marimo/02_03_counting_mapped_annotated_reads.html) |
| [`02_04_exploratory_data_analysis.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_04_exploratory_data_analysis.py) | [Open](../marimo/02_04_exploratory_data_analysis.html) |
| [`02_05_differential_analysis.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_05_differential_analysis.py) | [Open](../marimo/02_05_differential_analysis.html) |
| [`02_06_enrichment_analysis.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_06_enrichment_analysis.py) | [Open](../marimo/02_06_enrichment_analysis.html) |
| [`02_07_cross_validation.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/02_07_cross_validation.py) | [Open](../marimo/02_07_cross_validation.html) |

## Machine Learning

| Source notebook | WASM export |
| --- | --- |
| [`03_01_what_is_machine_learning.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/03_01_what_is_machine_learning.py) | [Open](../marimo/03_01_what_is_machine_learning.html) |
| [`03_02_exploratory_data_analysis.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/03_02_exploratory_data_analysis.py) | [Open](../marimo/03_02_exploratory_data_analysis.html) |
| [`03_03_implementing_ml_tools_and_decisions.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/03_03_implementing_ml_tools_and_decisions.py) | [Open](../marimo/03_03_implementing_ml_tools_and_decisions.html) |
| [`03_04_cross_validating_ml_tools.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/03_04_cross_validating_ml_tools.py) | [Open](../marimo/03_04_cross_validating_ml_tools.html) |
| [`03_05_from_ml_to_experimentation.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/03_05_from_ml_to_experimentation.py) | [Open](../marimo/03_05_from_ml_to_experimentation.html) |

## Molecular Design Engineering

| Source notebook | WASM export |
| --- | --- |
| [`04_01_techniques_strategies_molecular_design.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/04_01_techniques_strategies_molecular_design.py) | [Open](../marimo/04_01_techniques_strategies_molecular_design.html) |
| [`04_02_designing_first_molecular_library.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/04_02_designing_first_molecular_library.py) | [Open](../marimo/04_02_designing_first_molecular_library.html) |
| [`04_03_screening_first_molecular_library.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/04_03_screening_first_molecular_library.py) | [Open](../marimo/04_03_screening_first_molecular_library.html) |
| [`04_04_further_lead_hit_qc.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/04_04_further_lead_hit_qc.py) | [Open](../marimo/04_04_further_lead_hit_qc.html) |
| [`04_05_hit_selection_for_experimentation.py`](https://github.com/zfg2013/Codeguide/blob/main/notebooks/04_05_hit_selection_for_experimentation.py) | [Open](../marimo/04_05_hit_selection_for_experimentation.html) |

Add new notebooks as `notebooks/<name>.py`. The deployment workflow publishes `notebooks/my_notebook.py` as `marimo/my_notebook.html`.
