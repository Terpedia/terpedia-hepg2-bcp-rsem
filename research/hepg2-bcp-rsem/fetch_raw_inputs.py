"""Fetch checksum-pinned GSE276099 FASTQs and GENCODE v48 reference files."""

import argparse
import csv
import hashlib
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


PROJECT = Path(__file__).resolve().parent
DATA = PROJECT / "data" / "raw"
REFERENCE = {
    "GRCh38.primary_assembly.genome.fa.gz": (
        "https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_48/GRCh38.primary_assembly.genome.fa.gz",
        845635028,
        "42e38e8dd5027dd2ae8aeb8f3a990d07",
    ),
    "gencode.v48.primary_assembly.annotation.gtf.gz": (
        "https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_48/gencode.v48.primary_assembly.annotation.gtf.gz",
        59094311,
        "1b68ecb47fd4cc3946819fec58a59d8f",
    ),
}


def md5_file(path):
    digest = hashlib.md5()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fetch(path, url, size, md5):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and path.stat().st_size == size and md5_file(path) == md5:
        print(f"Verified existing {path}", flush=True)
        return
    if path.exists() and path.stat().st_size >= size:
        raise ValueError(f"Existing file has wrong checksum or length: {path}")
    subprocess.run(
        ["curl", "-fsSL", "--retry", "3", "-C", "-", "-o", str(path), url],
        check=True,
    )
    if path.stat().st_size != size or md5_file(path) != md5:
        raise ValueError(f"Downloaded file does not match source size and MD5: {path}")
    print(f"Verified {path}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("set", choices=("reference", "reads", "all"))
    parser.add_argument("--workers", type=int, default=3, help="parallel ENA downloads (1–6)")
    args = parser.parse_args()
    if not 1 <= args.workers <= 6:
        parser.error("--workers must be between 1 and 6")
    if args.set in ("reference", "all"):
        for name, (url, size, md5) in REFERENCE.items():
            fetch(DATA / "reference" / name, url, size, md5)
    if args.set in ("reads", "all"):
        with (PROJECT / "raw_run_manifest.tsv").open(newline="") as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
        if len(rows) != 6 or len({row["run_accession"] for row in rows}) != 6:
            raise ValueError("Expected six distinct runs in raw_run_manifest.tsv")
        downloads = []
        for row in rows:
            accession = row["run_accession"]
            url = row["fastq_url"]
            if not accession.startswith("SRR") or not accession[3:].isdigit() or not url.startswith("https://ftp.sra.ebi.ac.uk/") or not url.endswith(f"/{accession}.fastq.gz"):
                raise ValueError(f"Unexpected ENA run URL: {url}")
            downloads.append((DATA / "fastq" / f"{accession}.fastq.gz", url, int(row["fastq_bytes"]), row["fastq_md5"]))
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            list(pool.map(lambda item: fetch(*item), downloads))


if __name__ == "__main__":
    main()
