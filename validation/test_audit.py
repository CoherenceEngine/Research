import unittest, tempfile, shutil, csv, json
from pathlib import Path
import audit
class EvidenceAuditTests(unittest.TestCase):
    def test_preserves_mlp_failure(self):
        r=audit.models();self.assertEqual(r['passing'],8)
        self.assertFalse(next(x for x in r['models'] if x['model']=='MLP Neural Network')['operational_gate'])
    def test_invalid_counts_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp);shutil.copytree(audit.ROOT/'model_families_v1',p/'model_families_v1')
            f=p/'model_families_v1/aggregate_results.csv'
            with f.open() as inp: rows=list(csv.DictReader(inp))
            rows[0]['false_negatives']='17'
            with f.open('w',newline='') as out:
                w=csv.DictWriter(out,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
            with self.assertRaises(ValueError):audit.models(p)
    def test_nasa_missing_is_not_match(self):
        self.assertEqual(audit.nasa()['status'],'OUTPUTS_MISSING_OR_MISMATCH')
    def test_nasa_wrong_bytes_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            d=json.loads((audit.ROOT/'nasa_fd002_fd004_v1/reference_receipt.json').read_text())
            for n in d['canonical_result_hashes']: (Path(tmp)/n).write_text('wrong')
            self.assertTrue(all(v=='MISMATCH' for v in audit.nasa(tmp)['files'].values()))
    def test_hbi_rounded_arithmetic(self):
        self.assertAlmostEqual(audit.hbi()['recomputed_percent']['mean_modeled_energy'],20.23308,places=4)
if __name__=='__main__':unittest.main()
