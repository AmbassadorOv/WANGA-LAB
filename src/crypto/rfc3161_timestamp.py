from __future__ import annotations
import subprocess
from pathlib import Path

def request_timestamp(input_file: str | Path, tsr_file: str | Path, tsa_url: str) -> None:
    query = Path(str(tsr_file) + ".tsq")
    subprocess.run(["openssl","ts","-query","-data",str(input_file),"-sha256","-cert","-out",str(query)], check=True)
    try:
        subprocess.run(["openssl","ts","-reply","-queryfile",str(query),"-token_out","-out",str(tsr_file),"-url",tsa_url], check=True)
    finally:
        query.unlink(missing_ok=True)

def verify_timestamp(input_file: str | Path, tsr_file: str | Path, ca_file: str | None = None, untrusted_file: str | None = None) -> None:
    cmd=["openssl","ts","-verify","-data",str(input_file),"-in",str(tsr_file)]
    if ca_file: cmd += ["-CAfile",ca_file]
    if untrusted_file: cmd += ["-untrusted",untrusted_file]
    subprocess.run(cmd, check=True)
