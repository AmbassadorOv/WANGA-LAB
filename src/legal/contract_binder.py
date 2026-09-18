from pathlib import Path
from src.crypto.sha256_chain import sha256_hex

def hash_file(path: str | Path) -> str:
    return sha256_hex(Path(path).read_bytes())

def bind_contract(package: dict, contract_path: str | Path) -> dict:
    out = dict(package)
    out["legal_binding"] = {"contract_sha256": hash_file(contract_path), "binding_method":"SHA-256 of exact contract bytes"}
    return out
