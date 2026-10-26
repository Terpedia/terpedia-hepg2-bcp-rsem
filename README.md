# Terpedia HepG2 β-caryophyllene transcriptomics audit

This forkable project audits the [GEO GSE276099](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099) deposited expression matrix for three ethanol-vehicle and three β-caryophyllene HepG2 **bulk RNA-seq** libraries. It includes an [executed Jupyter notebook](notebooks/terputer-hepg2-bcp-rsem.ipynb), [claim-linked report](research/hepg2-bcp-rsem/generated/white-paper.md), [claim ledger](research/hepg2-bcp-rsem/generated/claim-ledger.tsv), [result tables](research/hepg2-bcp-rsem/results), and [notebook execution receipt](research/execution-receipts/terputer-hepg2-bcp-rsem.json).

The matrix has 17,034 analyzable numeric-gene rows after excluding 20 blank gene-set-like rows. Its values are predominantly fractional. The notebook describes sample QC, log1p(CPM) correlations, pseudocount-sensitive group-mean ratios, and the five PGF/MAPK genes discussed by the [source article](https://doi.org/10.3389/fphar.2024.1492670). It does **not** reproduce the paper's 433-DEG model, infer statistical significance, establish direct target binding, or supply single-cell or genetic Perturb-seq evidence. GEO sample dose fields vary 150/151/152 µM although the common protocol says 150 µM for 24 hours.

## Reproduce

Use Python 3.10 or newer and Node.js:

```sh
python -m pip install -r requirements.txt
python restore-inputs.py research/hepg2-bcp-rsem/report-spec.json
python notebook-runner.py notebooks/terputer-hepg2-bcp-rsem.ipynb . 120 '["research/hepg2-bcp-rsem/results/analysis_summary.json","research/hepg2-bcp-rsem/results/sample_qc.tsv","research/hepg2-bcp-rsem/results/sample_correlations.tsv","research/hepg2-bcp-rsem/results/descriptive_effects.tsv"]' '["research/hepg2-bcp-rsem/analysis.py","research/hepg2-bcp-rsem/sample_manifest.tsv","research/hepg2-bcp-rsem/data/GSE276099_readCounts.csv.gz"]'
node report-generator.mjs research/hepg2-bcp-rsem/report-spec.json
```

The GEO download is checksum pinned and excluded from Git. `restore-inputs.py` checks the download against the report specification. To attach this project to a `terpedia-report` workspace, fork this repository under the same name and use `add_research_project_submodule` with slug `hepg2-bcp-rsem`; the path is `projects/hepg2-bcp-rsem`.

The [ENA raw-run manifest](research/hepg2-bcp-rsem/raw_run_manifest.tsv) maps the six GEO libraries to source-reported FASTQs. The [NCBI SRA manifest](research/hepg2-bcp-rsem/sra_run_manifest.tsv) pins the normalized SRA archives selected for retrieval and records Data Locator MD5 values. The saved notebook and report remain descriptive until conversion, alignment, QC, and model outputs are executed and reviewed.

An [unexecuted raw-count notebook](notebooks/terputer-hepg2-bcp-raw-counts.ipynb) now specifies sample QC and a two-arm PyDESeq2 model for the planned STAR count matrix. Its separate [dependency lock](requirements-raw-counts.lock.txt) records the analysis environment. It is a method draft until the downloaded reads, mapping QC, saved outputs, and notebook execution receipt are present; the linked white paper above still reports only the fractional-matrix audit.

See the [project methods and interpretation](research/hepg2-bcp-rsem/README.md).
