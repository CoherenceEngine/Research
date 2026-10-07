from pathlib import Path
import gzip, base64
root=Path(__file__).parent
for name in ["scania_decisions.json", "hbi_trajectories.json"]:
    (root/name).write_bytes(gzip.decompress(base64.b64decode((root/(name+".gz.b64")).read_text())))
print("Decoded recorded viewer data. Serve this folder with python -m http.server")
