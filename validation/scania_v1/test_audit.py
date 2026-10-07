import base64
import copy
import gzip
import json
import unittest
from pathlib import Path
from audit import audit

ROOT = Path(__file__).resolve().parent

class AuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT/'manifest.json').read_text())
        cls.raw = gzip.decompress(base64.b64decode((ROOT/'decisions.csv.gz.b64').read_text()))

    def test_reference_and_same_misses(self):
        result = audit(self.raw, self.manifest)
        self.assertEqual(result['metrics']['gate_v2']['modeled_cost'], 10400)
        self.assertEqual(result['heavy_calls_avoided'], 13708)
        self.assertEqual(result['newly_missed_rows'], [])

    def test_tamper_rejected(self):
        with self.assertRaises(ValueError):
            audit(self.raw+b'\n', self.manifest)

    def test_duplicate_rejected_even_without_hash(self):
        rows=self.raw.decode().splitlines()
        rows[2]=rows[1]
        with self.assertRaises(ValueError):
            audit(('\n'.join(rows)+'\n').encode(), self.manifest, False)

    def test_nonbinary_rejected(self):
        rows=self.raw.decode().splitlines()
        fields=rows[1].split(','); fields[1]='2'; rows[1]=','.join(fields)
        with self.assertRaises(ValueError):
            audit(('\n'.join(rows)+'\n').encode(), self.manifest, False)

    def test_prediction_change_fails_reference(self):
        rows=self.raw.decode().splitlines()
        fields=rows[1].split(',');fields[4]=str(1-int(fields[4]));rows[1]=','.join(fields)
        with self.assertRaises(ValueError):
            audit(('\n'.join(rows)+'\n').encode(), self.manifest, False)

    def test_missing_row_rejected(self):
        with self.assertRaises(ValueError):
            audit(b'\n'.join(self.raw.splitlines()[:-1])+b'\n',self.manifest,False)

if __name__ == '__main__':
    unittest.main()
