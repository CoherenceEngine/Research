"""Audit released decisions; this does not execute The Coherence Engine."""
import argparse
import base64
import csv
import gzip
import hashlib
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
FIELDS = ['row_index', 'actual_failure', 'coherence_gate_calls_heavy', 'baseline_prediction', 'coherence_v2_prediction']

def audit(raw, manifest, check_hash=True):
    if check_hash and hashlib.sha256(raw).hexdigest() != manifest['released_csv_sha256']:
        raise ValueError('Released ledger hash mismatch')
    reader = csv.DictReader(io.StringIO(raw.decode('utf-8'), newline=''))
    if reader.fieldnames != FIELDS:
        raise ValueError('Unexpected ledger schema')
    rows = list(reader)
    if len(rows) != manifest['rows']:
        raise ValueError('Unexpected row count')
    seen = set()
    counts = {name: dict(tp=0, tn=0, fp=0, fn=0) for name in ['always_on', 'gate_v2']}
    heavy = 0
    baseline_misses, gated_misses = set(), set()
    for row in rows:
        idx = int(row['row_index'])
        if str(idx) != row['row_index'] or idx in seen or not 0 <= idx < manifest['rows']:
            raise ValueError('Duplicate, invalid, or out-of-range row index')
        seen.add(idx)
        for field in FIELDS[1:]:
            if row[field] not in ('0', '1'):
                raise ValueError('Nonbinary field: ' + field)
        y = int(row['actual_failure'])
        heavy += int(row['coherence_gate_calls_heavy'])
        for name, field, misses in [('always_on', 'baseline_prediction', baseline_misses), ('gate_v2', 'coherence_v2_prediction', gated_misses)]:
            pred = int(row[field])
            key = 'tp' if y and pred else 'fn' if y else 'fp' if pred else 'tn'
            counts[name][key] += 1
            if key == 'fn':
                misses.add(idx)
    for name, calls in [('always_on', len(rows)), ('gate_v2', heavy)]:
        m = counts[name]
        m['modeled_cost'] = 10*m['fp'] + 500*m['fn']
        m['heavy_calls'] = calls
        m['recall'] = m['tp'] / (m['tp'] + m['fn']) if m['tp'] + m['fn'] else None
    for name, expected in manifest['expected'].items():
        for key, value in expected.items():
            if counts[name][key] != value:
                raise ValueError('Reference mismatch: ' + name + '.' + key)
    return dict(status='LEDGER_AUDIT_PASS', validation_scope='decision-ledger arithmetic only', rows=len(rows), released_csv_sha256=hashlib.sha256(raw).hexdigest(), metrics=counts, heavy_calls_avoided=len(rows)-heavy, heavy_call_reduction_pct=100*(len(rows)-heavy)/len(rows), newly_missed_rows=sorted(gated_misses-baseline_misses), recovered_missed_rows=sorted(baseline_misses-gated_misses), engine_executed=False, external_reviewer_execution=False, physical_energy_measured=False)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    manifest = json.loads((ROOT/'manifest.json').read_text())
    compressed = base64.b64decode(''.join((ROOT/'decisions.csv.gz.b64').read_text().split()), validate=True)
    if hashlib.sha256(compressed).hexdigest() != manifest['released_gzip_sha256']:
        raise SystemExit('Compressed ledger hash mismatch')
    result = audit(gzip.decompress(compressed), manifest)
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(rendered + '\n')
    print(rendered)

if __name__ == '__main__':
    main()
