# β-Caryophyllene exposure in HepG2: an executed processed-count audit

> Generated evidence brief. Each statement is linked to a claim record; scientific interpretation still requires review.

**Research question:** Which metabolic and signaling responses to terpene exposure are reproducible, and which depend on cellular context or a specific target?

**Notebook:** `notebooks/terputer-hepg2-bcp-rsem.ipynb` · SHA-256 `e24dba7f840748ae81e3f607be7c033d1af511cbce5c0f17733672d888fbbfa4` · 1 executed code cells

## Abstract

**Observed in notebook:** The pinned supplementary file has 17,054 rows; 17,034 rows have numeric gene IDs and six complete nonnegative columns. Twenty gene-set-like rows have all six count cells blank, and 75,830 retained numeric entries are fractional. (claim C02; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz), [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099))

**Observed in notebook:** Among 12,321 genes with mean CPM at least 1 in either arm, descriptive group-mean ratios with a 0.1 CPM pseudocount place 74 at least twofold higher and 146 at least twofold lower after exposure; a 1.0 CPM pseudocount gives 34 higher and 79 lower. (claim C04; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz))

**Observed in notebook:** PGF mean CPM is 1.924 in vehicle and 0.760 after β-caryophyllene, a descriptive log2 ratio of -1.235 with a 0.1 CPM pseudocount. NR4A1 and CSF1R trend higher, while ARTN and CACNA1E trend lower in the same matrix. (claim C05; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz), [3](https://doi.org/10.3389/fphar.2024.1492670))

## Background

**Source-reported:** GSE276099 contains three HepG2 ethanol-vehicle and three β-caryophyllene bulk RNA-seq libraries. The common sample protocol says 150 µM for 24 hours, whereas the per-sample treatment fields show 150, 151, and 152 µM in replicate order for both arms. (claim C01; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099))

**Source-reported:** The source article reports 433 protein-coding DEGs and a PGF/MAPK-related response, including a PGF overexpression experiment that changed β-caryophyllene sensitivity. (claim C06; [3](https://doi.org/10.3389/fphar.2024.1492670), [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099))

## Methods

**Observed in notebook:** The pinned supplementary file has 17,054 rows; 17,034 rows have numeric gene IDs and six complete nonnegative columns. Twenty gene-set-like rows have all six count cells blank, and 75,830 retained numeric entries are fractional. (claim C02; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz), [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/sample_qc.tsv](../results/sample_qc.tsv).

**Observed in notebook:** Across the 17,034 retained genes, median pairwise Pearson correlations of log1p(CPM) are 0.994 within controls, 0.998 within treated libraries, and 0.994 between arms. (claim C03; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/sample_correlations.tsv](../results/sample_correlations.tsv).

**Observed in notebook:** Among 12,321 genes with mean CPM at least 1 in either arm, descriptive group-mean ratios with a 0.1 CPM pseudocount place 74 at least twofold higher and 146 at least twofold lower after exposure; a 1.0 CPM pseudocount gives 34 higher and 79 lower. (claim C04; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/descriptive_effects.tsv](../results/descriptive_effects.tsv).

## Results

**Observed in notebook:** Across the 17,034 retained genes, median pairwise Pearson correlations of log1p(CPM) are 0.994 within controls, 0.998 within treated libraries, and 0.994 between arms. (claim C03; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/sample_correlations.tsv](../results/sample_correlations.tsv). **Limitation:** CPM is scaled from the retained gene rows. High correlations neither establish biological replication nor exclude treatment effects.

**Observed in notebook:** Among 12,321 genes with mean CPM at least 1 in either arm, descriptive group-mean ratios with a 0.1 CPM pseudocount place 74 at least twofold higher and 146 at least twofold lower after exposure; a 1.0 CPM pseudocount gives 34 higher and 79 lower. (claim C04; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/descriptive_effects.tsv](../results/descriptive_effects.tsv). **Limitation:** These pseudocount-sensitive counts are not differentially expressed gene calls and have no fitted variance or adjusted p-values.

**Observed in notebook:** PGF mean CPM is 1.924 in vehicle and 0.760 after β-caryophyllene, a descriptive log2 ratio of -1.235 with a 0.1 CPM pseudocount. NR4A1 and CSF1R trend higher, while ARTN and CACNA1E trend lower in the same matrix. (claim C05; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz), [3](https://doi.org/10.3389/fphar.2024.1492670)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/descriptive_effects.tsv](../results/descriptive_effects.tsv). **Limitation:** This confirms only direction in the deposited matrix, not statistical significance, MAPK pathway activity, direct molecular binding, or the paper's PGF rescue experiment.

## Interpretation

**Observed in notebook:** PGF mean CPM is 1.924 in vehicle and 0.760 after β-caryophyllene, a descriptive log2 ratio of -1.235 with a 0.1 CPM pseudocount. NR4A1 and CSF1R trend higher, while ARTN and CACNA1E trend lower in the same matrix. (claim C05; [2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz), [3](https://doi.org/10.3389/fphar.2024.1492670)) Artifacts: [research/hepg2-bcp-rsem/results/analysis_summary.json](../results/analysis_summary.json), [research/hepg2-bcp-rsem/results/descriptive_effects.tsv](../results/descriptive_effects.tsv). **Limitation:** This confirms only direction in the deposited matrix, not statistical significance, MAPK pathway activity, direct molecular binding, or the paper's PGF rescue experiment.

**Source-reported:** The source article reports 433 protein-coding DEGs and a PGF/MAPK-related response, including a PGF overexpression experiment that changed β-caryophyllene sensitivity. (claim C06; [3](https://doi.org/10.3389/fphar.2024.1492670), [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099)) **Limitation:** The notebook does not reproduce the original differential-expression model, pathway analysis, or functional experiment. The reported response does not establish direct ligand binding to PGF.

## Limitations

**Claim C01 (source-reported):** GSE276099 contains three HepG2 ethanol-vehicle and three β-caryophyllene bulk RNA-seq libraries. The common sample protocol says 150 µM for 24 hours, whereas the per-sample treatment fields show 150, 151, and 152 µM in replicate order for both arms. **Limitation:** The archive does not explain the replicate dose-field discrepancy; do not infer a deliberate dose series. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099))

**Claim C02 (observed):** The pinned supplementary file has 17,054 rows; 17,034 rows have numeric gene IDs and six complete nonnegative columns. Twenty gene-set-like rows have all six count cells blank, and 75,830 retained numeric entries are fractional. **Limitation:** The deposited file is described as read counts, but its fractional values are processed estimates, not independent evidence of integer raw counts. ([2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz), [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099))

**Claim C04 (observed):** Among 12,321 genes with mean CPM at least 1 in either arm, descriptive group-mean ratios with a 0.1 CPM pseudocount place 74 at least twofold higher and 146 at least twofold lower after exposure; a 1.0 CPM pseudocount gives 34 higher and 79 lower. **Limitation:** These pseudocount-sensitive counts are not differentially expressed gene calls and have no fitted variance or adjusted p-values. ([2](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz))

**Claim C08 (proposed):** Study β-caryophyllene in additional cell types or states with matched vehicle controls and target perturbations before calling the PGF/MAPK response reproducible or target-dependent across cellular contexts. **Limitation:** This cohort contains one human cell line, one treatment condition, and no genetic Perturb-seq contrast. ([1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [3](https://doi.org/10.3389/fphar.2024.1492670))

## Next research steps

**Proposed:** Obtain the six original sequencing runs and a pinned human annotation, clarify dose metadata, and fit a prespecified count model with biological-replicate uncertainty. Compare the inferred effect with the deposited matrix and reported 433-DEG list. (claim C07; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [3](https://doi.org/10.3389/fphar.2024.1492670))

**Proposed:** Study β-caryophyllene in additional cell types or states with matched vehicle controls and target perturbations before calling the PGF/MAPK response reproducible or target-dependent across cellular contexts. (claim C08; [1](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099), [3](https://doi.org/10.3389/fphar.2024.1492670))

## Data and code availability

The source specification is `research/hepg2-bcp-rsem/report-spec.json` (SHA-256 `b7105dfca82fff37727f8756b137e9792cbc66d86708f98631fef4d516df926e`). The claim ledger and generation receipt accompany this report. File hashes identify the report files and cited result artifacts. 1 externally sourced input file has a source URL and hash listed below. The [notebook execution receipt](../../execution-receipts/terputer-hepg2-bcp-rsem.json) matches the saved notebook and records hashes for result files written during its fresh-kernel run. It also pins 3 declared local input files by SHA-256. It records the Python version and installed package versions. Notebook execution does not independently validate scientific interpretation.

### External data files

The following download locations and file hashes match inputs pinned by the notebook execution receipt. The generator does not download these files or verify that the URLs remain live.

| Input | Download | SHA-256 |
| --- | --- | --- |
| `research/hepg2-bcp-rsem/data/GSE276099_readCounts.csv.gz` | [Source file](https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz) | `0b9c79088d962c49b0bbd3832a98646daba23985c51f4153cc4f938151c98aeb` |

## References

[1] GEO GSE276099 series and six sample records. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE276099
[2] GSE276099 supplementary readCounts matrix. https://ftp.ncbi.nlm.nih.gov/geo/series/GSE276nnn/GSE276099/suppl/GSE276099_readCounts.csv.gz
[3] Basheer et al., β-caryophyllene and MAPK signaling in HCC (2024). https://doi.org/10.3389/fphar.2024.1492670
