import json,hashlib,csv
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def check():
 manifest=json.loads((ROOT/'manifest.json').read_text())
 for n,h in manifest['files'].items():
  if hashlib.sha256((ROOT/n).read_bytes()).hexdigest()!=h:raise ValueError('Hash mismatch: '+n)
 receipt=json.loads((ROOT.parent/'validation/nasa_fd002_fd004_v1/reference_receipt.json').read_text())
 for n,h in receipt['canonical_result_hashes'].items():
  if hashlib.sha256((ROOT/('nasa_'+n)).read_bytes()).hexdigest()!=h:raise ValueError('NASA archived hash mismatch')
 with (ROOT/'hbi_per_scenario.csv').open() as f:rows=list(csv.DictReader(f))
 if len(rows)!=144:raise ValueError('Expected 144 policy rows')
 summary=json.loads((ROOT/'hbi_summary.json').read_text())
 for policy in ['bellman','event_v041']:
  selected=[r for r in rows if r['policy']==policy]
  if {int(r['scenario']) for r in selected}!=set(range(1,73)):raise ValueError('Scenario identity mismatch')
  for key,col in [('mean_energy','total_energy'),('mean_command_events','command_events'),('mean_active_steps','active_steps')]:
   if abs(sum(float(r[col]) for r in selected)/72-summary['policies'][policy][key])>1e-9:raise ValueError('Summary mismatch')
  if sum(int(r['survived']) for r in selected)!=72 or sum(int(r['safety_violations']) for r in selected)!=0:raise ValueError('Safety outcome mismatch')
 scania=json.loads((ROOT/'scania_local_replay_receipt.json').read_text())
 if scania['rows']!=16000 or any(scania['decision_mismatches'].values()):raise ValueError('Scania replay mismatch receipt')
 return {'file_integrity':'MATCH','nasa_archived_csvs':6,'hbi_cases':72,'hbi_policies':2,'scania_receipt':'zero decision mismatches','scope':'output audit only, no engine execution by this script'}
if __name__=='__main__':print(json.dumps(check(),indent=2))
