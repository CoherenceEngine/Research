"""Audit released evidence only, never executes The Coherence Engine."""
import argparse, csv, hashlib, json, math
from pathlib import Path
ROOT = Path(__file__).resolve().parent
def models(root=ROOT):
    with (root/'model_families_v1/aggregate_results.csv').open() as f:
        rows=list(csv.DictReader(f))
    groups={}
    for r in rows: groups.setdefault(r['model'],[]).append(r)
    if len(groups)!=9 or len(rows)!=18: raise ValueError('Expected nine paired models')
    results=[]
    for model,pair in groups.items():
        if len(pair)!=2: raise ValueError('Unpaired model')
        b=[r for r in pair if r['configuration']=='Full model on every record']
        g=[r for r in pair if r['configuration']=='Δ.72 coherence gate + full model']
        if len(b)!=1 or len(g)!=1: raise ValueError('Invalid configurations')
        b,g=b[0],g[0]
        for r in (b,g):
            tp,tn,fp,fn=[int(r[k]) for k in ('true_positives','true_negatives','false_positives','false_negatives')]
            calls=int(r['full_model_calls'])
            if min(tp,tn,fp,fn,calls)<0 or tp+tn+fp+fn!=16000 or tp+fn!=375 or calls>16000:raise ValueError('Invalid population')
            if int(r['modeled_cost'])!=10*fp+500*fn:raise ValueError('Cost mismatch')
            expected={'recall':tp/(tp+fn),'precision':tp/(tp+fp),'f1':2*tp/(2*tp+fp+fn),'balanced_accuracy':(tp/(tp+fn)+tn/(tn+fp))/2,'full_model_calls_avoided':16000-calls,'full_model_call_reduction_pct':100*(16000-calls)/16000}
            for k,v in expected.items():
                if not math.isclose(float(r[k]),v,abs_tol=1e-9):raise ValueError('Metric mismatch: '+k)
        if int(b['full_model_calls'])!=16000:raise ValueError('Baseline calls mismatch')
        cost_change=100*(int(g['modeled_cost'])/int(b['modeled_cost'])-1)
        missed=int(g['false_negatives'])-int(b['false_negatives'])
        passed=float(g['full_model_call_reduction_pct'])>=25 and cost_change<=2 and missed<=1
        if not math.isclose(cost_change,float(g['relative_cost_change_pct']),abs_tol=1e-9) or missed!=int(g['missed_failure_change']) or passed!=(g['passes_operational_gate']=='True'):raise ValueError('Gate mismatch')
        results.append({'model':model,'operational_gate':passed,'additional_misses':missed,'cost_change_pct':cost_change})
    return {'scope':'aggregate arithmetic, no engine execution','models':results,'passing':sum(r['operational_gate'] for r in results)}
def hbi(root=ROOT):
    d=json.loads((root/'hbi_v0_4_1/reference_summary.json').read_text())
    reductions={k:100*(1-d['event_v0_4_1'][k]/d['bellman'][k]) for k in ('mean_modeled_energy','mean_command_events','mean_active_steps')}
    return {'scope':'rounded summary arithmetic, simulation only','recomputed_percent':reductions,'case_level_evidence':'NOT_RELEASED'}
def nasa(artifacts=None,root=ROOT):
    d=json.loads((root/'nasa_fd002_fd004_v1/reference_receipt.json').read_text())
    results={}
    for name,expected in d['canonical_result_hashes'].items():
        f=Path(artifacts)/name if artifacts else None
        results[name]='MISSING' if f is None or not f.is_file() else ('MATCH' if hashlib.sha256(f.read_bytes()).hexdigest()==expected else 'MISMATCH')
    return {'scope':'archived output byte comparison, no engine execution','status':'EXACT_HASH_MATCH' if all(v=='MATCH' for v in results.values()) else 'OUTPUTS_MISSING_OR_MISMATCH','files':results}
def integrity(root=ROOT):
    m=json.loads((root/'portfolio_manifest.json').read_text())
    for p,h in m['files'].items():
        f=root.parent/p
        if not f.is_file() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:raise ValueError('Integrity mismatch: '+p)
    return {'hashed_files':len(m['files']),'status':'MATCH','limit':'Manifest integrity does not prove authorship or independent execution'}
def main():
    p=argparse.ArgumentParser();p.add_argument('scope',choices=['all','models','hbi','nasa']);p.add_argument('--artifacts');a=p.parse_args()
    r={'integrity':integrity()}
    if a.scope in ('all','models'):r['models']=models()
    if a.scope in ('all','hbi'):r['hbi']=hbi()
    if a.scope in ('all','nasa'):r['nasa']=nasa(a.artifacts)
    print(json.dumps(r,indent=2))
    if a.scope=='nasa' and r['nasa']['status']!='EXACT_HASH_MATCH':raise SystemExit(2)
if __name__=='__main__':main()
