from src.crypto.sha256_chain import build_chain, verify_chain

def test_chain_is_deterministic():
    a,b,c={"usd":100},{"asset":"screw"},{"recovery":25}
    chain=build_chain(a,b,c,"2026-09-18T00:00:00Z")
    assert chain == build_chain(a,b,c,"2026-09-18T00:00:00Z")
    assert verify_chain({"exposure":a,"screw":b,"recovery":c,"chain":chain})

def test_change_breaks_chain():
    a,b,c={"usd":100},{"asset":"screw"},{"recovery":25}
    chain=build_chain(a,b,c,"2026-09-18T00:00:00Z")
    a["usd"]=101
    assert not verify_chain({"exposure":a,"screw":b,"recovery":c,"chain":chain})
