# Terpedia HepG2 β-caryophyllene transcriptomics audit

This forkable project audits [GEO GSE276099](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), with three ethanol-vehicle and three β-caryophyllene HepG2 **bulk RNA-seq** libraries. It includes a [raw-count Jupyter notebook](notebooks/terputer-hepg2-bcp-raw-counts.ipynb), [claim-linked raw-count report](research/hepg2-bcp-raw-counts/generated/white-paper.md), [result tables](research/hepg2-bcp-rsem/results/raw_counts), and [execution receipt](research/execution-receipts/terputer-hepg2-bcp-raw-counts.json). The earlier [processed-matrix notebook](notebooks/terputer-hepg2-bcp-rsem.ipynb) and [audit report](research/hepg2-bcp-rsem/generated/white-paper.md) remain available separately.

The deposited matrix has 17,034 analyzable numeric-gene rows after excluding 20 blank gene-set-like rows, and its values are predominantly fractional. Reprocessing all six raw runs against GENCODE v48 produced 78,894 unstranded integer gene-count rows. The prespecified PyDESeq2 contrast tested 15,078 genes and found 1,616 at adjusted p below 0.05, including PGF, NR4A1, CSF1R, ARTN, and CACNA1E. This one-cohort estimate does **not** reproduce the [source article's](https://doi.org/10.3389/fphar.2024.1492670) exact 433-DEG model, establish direct target binding, or supply single-cell or genetic Perturb-seq evidence. GEO sample dose fields vary 150/151/152 µM although the common protocol says 150 µM for 24 hours.

## Reproduce

Use Python 3.10 or newer and Node.js:

```sh
python -m pip install -r requirements.txt
python restore-inputs.py research/hepg2-bcp-rsem/report-spec.json
python notebook-runner.py notebooks/terputer-hepg2-bcp-rsem.ipynb . 120 '["research/hepg2-bcp-rsem/results/analysis_summary.json","research/hepg2-bcp-rsem/results/sample_qc.tsv","research/hepg2-bcp-rsem/results/sample_correlations.tsv","research/hepg2-bcp-rsem/results/descriptive_effects.tsv"]' '["research/hepg2-bcp-rsem/analysis.py","research/hepg2-bcp-rsem/sample_manifest.tsv","research/hepg2-bcp-rsem/data/GSE276099_readCounts.csv.gz"]'
node report-generator.mjs research/hepg2-bcp-rsem/report-spec.json
```

The GEO download is checksum pinned and excluded from Git. `restore-inputs.py` checks the download against the report specification. To attach this project to a `terpedia-report` workspace, fork this repository under the same name and use `add_research_project_submodule` with slug `hepg2-bcp-rsem`; the path is `projects/hepg2-bcp-rsem`.

The [ENA raw-run manifest](research/hepg2-bcp-rsem/raw_run_manifest.tsv) maps the six GEO libraries to source-reported FASTQs. The [NCBI SRA manifest](research/hepg2-bcp-rsem/sra_run_manifest.tsv) pins the normalized SRA archives selected for retrieval and records Data Locator MD5 values. The [conversion](research/hepg2-bcp-rsem/results/raw_counts/conversion_receipt.json), [processing](research/hepg2-bcp-rsem/results/raw_counts/processing_receipt.json), and [notebook](research/execution-receipts/terputer-hepg2-bcp-raw-counts.json) receipts link those inputs to the reported estimates.

The [raw-count notebook](notebooks/terputer-hepg2-bcp-raw-counts.ipynb) records sample QC and the two-arm PyDESeq2 model. Its separate [dependency lock](requirements-raw-counts.lock.txt) records the analysis environment. To reproduce the count-based report after preparing the pinned raw inputs, run `python research/hepg2-bcp-rsem/run_raw_count_notebook.py` in that environment, then `node report-generator.mjs research/hepg2-bcp-rsem/raw-count-report-spec.json`.

See the [project methods and interpretation](research/hepg2-bcp-rsem/README.md).
