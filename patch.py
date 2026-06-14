import site
from pathlib import Path

candidates = site.getsitepackages() + [site.getusersitepackages()]
target = next(
    (Path(p) / "fairseq" / "checkpoint_utils.py" for p in candidates
     if (Path(p) / "fairseq" / "checkpoint_utils.py").exists()),
    None,
)
if target is None:
    print("No se encontró fairseq en ninguna ruta de site-packages.")
    exit(1)

content = target.read_text(encoding="utf-8")
old = 'state = torch.load(f, map_location=torch.device("cpu"))'
new = 'state = torch.load(f, map_location=torch.device("cpu"), weights_only=False)'

if new in content:
    print("El parche ya estaba aplicado.")
elif old in content:
    target.write_text(content.replace(old, new), encoding="utf-8")
    print(f"Parche aplicado en {target}")
else:
    print("No se encontró la línea a parchear. Puede que la versión de fairseq sea distinta.")
    print(f"Revisa manualmente: {target}")