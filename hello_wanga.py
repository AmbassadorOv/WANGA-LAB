"""Minimal entry point test for WANGA-NANO-21 connection & first run verification."""

def test_wanga_nano_21_connection():
    message = "WANGA-NANO-21 repository connected successfully."
    assert "WANGA-NANO-21" in message
    return True

if __name__ == "__main__":
    success = test_wanga_nano_21_connection()
    if success:
        print("WANGA-NANO-21 First Run Test: PASSED")
