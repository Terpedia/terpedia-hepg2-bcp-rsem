"""Descriptive, non-inferential audit of GEO GSE276099 processed fractional counts."""
from pathlib import Path
from itertools import combinations
import csv
import gzip
import hashlib
import json
import math
import statistics

ROOT = Path('research/hepg2-bcp-rsem')
MATRIX = ROOT / 'data/GSE276099_readCounts.csv.gz'
MANIFEST = ROOT / 'sample_manifest.tsv'
RESULTS = ROOT / 'results'
RESULTS.mkdir(parents=True, exist_ok=True)
EXPECTED_SHA256 = '0b9c79088d962c49b0bbd3832a98646daba23985c51f4153cc4f938151c98aeb'
assert hashlib.sha256(MATRIX.read_bytes()).hexdigest() == EXPECTED_SHA256
with MANIFEST.open(newline='') as stream:
    samples = list(csv.DictReader(stream, delimiter='\t'))
columns = [s['matrix_column'] for s in samples]
assert columns == [f'read_count_{arm}{i}' for arm in ('C', 'T') for i in (1, 2, 3)]
assert [s['arm'] for s in samples] == ['control'] * 3 + ['bcp'] * 3

valid = []
excluded = []
with gzip.open(MATRIX, 'rt', encoding='utf-8-sig', newline='') as stream:
    reader = csv.DictReader(stream)
    assert reader.fieldnames == ['gene_id', 'gene_symbol', *columns]
    for row in reader:
        if not row['gene_id'].isdigit() or any(not row[column] for column in columns):
            excluded.append({'gene_id_prefix': row['gene_id'][:60], 'reason': 'nonnumeric gene ID or blank sample value'})
            continue
        values = [float(row[column]) for column in columns]
        assert all(math.isfinite(v) and v >= 0 for v in values)
        valid.append((row['gene_id'], row['gene_symbol'], values))
assert len(valid) == 17034 and len(excluded) == 20
assert len({gene_id for gene_id, _, _ in valid}) == len(valid)

totals = [sum(values[i] for _, _, values in valid) for i in range(6)]
assert all(total > 0 for total in totals)
fractional = [sum(values[i] != int(values[i]) for _, _, values in valid) for i in range(6)]
with (RESULTS / 'sample_qc.tsv').open('w', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['matrix_column', 'geo_accession', 'arm', 'treatment_field', 'total_processed_count', 'fractional_entries', 'genes_with_nonzero_value'])
    for i, sample in enumerate(samples):
        writer.writerow([columns[i], sample['geo_accession'], sample['arm'], sample['treatment_field'], f'{totals[i]:.4f}', fractional[i], sum(values[i] > 0 for _, _, values in valid)])

# CPM uses the six column sums of the retained rows; it is a descriptive scaling, not a fitted count model.
cpm = [[values[i] * 1_000_000 / totals[i] for i in range(6)] for _, _, values in valid]
log_cpm = [[math.log1p(value) for value in row] for row in cpm]
correlations = []
for i, j in combinations(range(6), 2):
    group = 'within_control' if i < 3 and j < 3 else 'within_treated' if i >= 3 and j >= 3 else 'between_arms'
    correlation = statistics.correlation([row[i] for row in log_cpm], [row[j] for row in log_cpm])
    correlations.append((columns[i], columns[j], group, correlation))
with (RESULTS / 'sample_correlations.tsv').open('w', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['sample_a', 'sample_b', 'group', 'pearson_log1p_cpm'])
    for a, b, group, value in correlations:
        writer.writerow([a, b, group, f'{value:.8f}'])

rows = []
for (gene_id, symbol, _), values in zip(valid, cpm, strict=True):
    control = statistics.mean(values[:3])
    treated = statistics.mean(values[3:])
    included = max(control, treated) >= 1
    ratio_01 = math.log2((treated + 0.1) / (control + 0.1))
    ratio_1 = math.log2((treated + 1.0) / (control + 1.0))
    rows.append((gene_id, symbol, control, treated, included, ratio_01, ratio_1))
with (RESULTS / 'descriptive_effects.tsv').open('w', newline='') as stream:
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['gene_id', 'gene_symbol', 'mean_control_cpm', 'mean_treated_cpm', 'included_max_mean_cpm_ge_1', 'log2_ratio_pseudocount_0_1', 'log2_ratio_pseudocount_1'])
    for gene_id, symbol, control, treated, included, ratio_01, ratio_1 in rows:
        writer.writerow([gene_id, symbol, f'{control:.6f}', f'{treated:.6f}', included, f'{ratio_01:.6f}', f'{ratio_1:.6f}'])

selected = [row for row in rows if row[4]]
marker_symbols = ['PGF', 'NR4A1', 'CSF1R', 'ARTN', 'CACNA1E']
markers = {symbol: [{'gene_id': gene_id, 'mean_control_cpm': control, 'mean_treated_cpm': treated, 'log2_ratio_0_1': effect} for gene_id, name, control, treated, _, effect, _ in rows if name == symbol] for symbol in marker_symbols}
summary = {
    'source_accession': 'GSE276099', 'assay': 'bulk RNA-seq processed RSEM-style fractional counts',
    'matrix_sha256': EXPECTED_SHA256, 'matrix_rows': len(valid) + len(excluded),
    'valid_numeric_gene_rows': len(valid), 'excluded_nonnumeric_or_blank_rows': len(excluded),
    'fractional_entries': sum(fractional), 'sample_count': len(samples),
    'library_totals_retained_rows': dict(zip(columns, totals, strict=True)),
    'included_gene_rows_max_arm_mean_cpm_ge_1': len(selected),
    'correlation_median_by_group': {group: statistics.median(value for _, _, g, value in correlations if g == group) for group in ['within_control', 'within_treated', 'between_arms']},
    'twofold_descriptive_count_pseudocount_0_1': {'higher': sum(row[5] >= 1 for row in selected), 'lower': sum(row[5] <= -1 for row in selected)},
    'twofold_descriptive_count_pseudocount_1': {'higher': sum(row[6] >= 1 for row in selected), 'lower': sum(row[6] <= -1 for row in selected)},
    'paper_marker_gene_descriptions': markers,
    'limitations': ['Processed fractional counts; no new differential expression or adjusted p-values', 'Six libraries from one HepG2 cell line; no cross-context replication', 'GEO per-sample dose fields show 150/151/152 µM although protocol says 150 µM', 'CPM and pseudocount thresholds are descriptive and sensitive to filtering'],
}
(RESULTS / 'analysis_summary.json').write_text(json.dumps(summary, indent=2) + '\n')
print(json.dumps({k: v for k, v in summary.items() if k not in ('library_totals_retained_rows', 'paper_marker_gene_descriptions')}, indent=2))
