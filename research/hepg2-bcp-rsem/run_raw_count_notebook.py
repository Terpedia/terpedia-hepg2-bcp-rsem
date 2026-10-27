"""Run the raw-count notebook as a Terputer research job with pinned inputs."""

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PREFIX = "research/hepg2-bcp-rsem"
RAW = f"{PREFIX}/results/raw_counts"
ARTIFACTS = [
    f"{RAW}/analysis_sample_qc.tsv",
    f"{RAW}/analysis_sample_correlations.tsv",
    f"{RAW}/analysis_sample_correlations.png",
    f"{RAW}/deseq2_results.tsv",
    f"{RAW}/prespecified_genes.tsv",
    f"{RAW}/analysis_summary.json",
]
INPUTS = [
    f"{RAW}/processing_receipt.json",
    f"{RAW}/conversion_receipt.json",
    f"{RAW}/gene_counts_unstranded.tsv.gz",
    f"{RAW}/gene_annotation.tsv.gz",
    f"{RAW}/star_mapping_qc.tsv",
    f"{PREFIX}/sra_run_manifest.tsv",
    f"{PREFIX}/sample_manifest.tsv",
    f"{PREFIX}/reprocess_star_counts.py",
]


def main() -> None:
    command = [
        sys.executable, str(ROOT / "notebook-runner.py"),
        "notebooks/terputer-hepg2-bcp-raw-counts.ipynb", str(ROOT), "7200",
        json.dumps(ARTIFACTS), json.dumps(INPUTS),
    ]
    subprocess.run(command, cwd=ROOT, check=True)


if __name__ == "__main__":
    main()
