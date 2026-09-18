from imperial_audit_core.src.core.commercial_quote import QuoteInputs, calculate_quote


def test_quote_is_reproducible():
    inputs = QuoteInputs(
        assets=10,
        jurisdictions=2,
        documents=100,
        verification_depth=3,
        integrations=1,
        annual_maintenance_rate=0.20,
    )
    kwargs = dict(
        setup_fee=1000,
        asset_fee=20,
        jurisdiction_fee=100,
        document_fee=2,
        verification_fee=150,
        integration_fee=500,
    )
    assert calculate_quote(inputs, **kwargs) == calculate_quote(inputs, **kwargs)


def test_quote_is_not_insurance_pricing():
    result = calculate_quote(
        QuoteInputs(assets=1, jurisdictions=1, documents=1, verification_depth=1, integrations=0),
        setup_fee=100,
        asset_fee=10,
        jurisdiction_fee=20,
        document_fee=5,
        verification_fee=25,
        integration_fee=0,
    )
    assert set(result) == {"setup_fee", "annual_maintenance_fee", "first_year_service_total"}


def test_invalid_scope_fails():
    try:
        calculate_quote(
            QuoteInputs(assets=0, jurisdictions=1, documents=0, verification_depth=0, integrations=0),
            setup_fee=100,
            asset_fee=10,
            jurisdiction_fee=20,
            document_fee=5,
            verification_fee=25,
            integration_fee=0,
        )
    except ValueError:
        return
    raise AssertionError("expected invalid scope to fail")
