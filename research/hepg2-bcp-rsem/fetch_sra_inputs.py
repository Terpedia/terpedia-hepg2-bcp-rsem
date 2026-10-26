"""Fetch NCBI SRA archives by accession and verify Data Locator MD5 values."""

import argparse
import csv
import subprocess
from concurrent.futures import ThreadPoolExecutor

from fetch_raw_inputs import DATA, PROJECT, md5_file


def fetch(row):
    accession = row["run_accession"]
    url = row["sra_url"]
    if not accession.startswith("SRR") or not accession[3:].isdigit() or url != f"https://sra-pub-run-odp.s3.amazonaws.com/sra/{accession}/{accession}":
        raise ValueError(f"Unexpected SRA accession or URL: {accession}")
    path = DATA / "sra" / f"{accession}.sra"
    expected_size = int(row["sra_bytes"])
    expected_md5 = row["sra_md5"]
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size == expected_size and md5_file(path) == expected_md5:
        print(f"Verified existing {accession}", flush=True)
        return
    if path.exists() and path.stat().st_size >= expected_size:
        raise ValueError(f"SRA archive has wrong size or checksum: {path}")
    subprocess.run(["curl", "-fsSL", "--retry", "3", "-C", "-", "-o", str(path), url], check=True)
    if path.stat().st_size != expected_size or md5_file(path) != expected_md5:
        raise ValueError(f"SRA archive does not match the NCBI Data Locator record: {path}")
    print(f"Verified {accession}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    if not 1 <= args.workers <= 6:
        parser.error("--workers must be between 1 and 6")
    with (PROJECT / "sra_run_manifest.tsv").open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    if len(rows) != 6 or len({row["run_accession"] for row in rows}) != 6:
        raise ValueError("Expected six distinct SRA runs")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        list(pool.map(fetch, rows))


if __name__ == "__main__":
    main()
