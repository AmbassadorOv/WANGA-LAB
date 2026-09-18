# Imperial Audit — Pricing Model V1

## Objective

Define a transparent service-fee model without implying that the fee itself constitutes insurance premium or creates coverage.

## Fee model

The base fee can scale with the verified asset value and the operational scope.

Example structure:

- Setup / evidence-capture fee: fixed amount by package complexity.
- Verification fee: percentage or fixed band based on verified asset value.
- Maintenance fee: recurring fee for periodic re-verification.
- Enterprise fee: negotiated according to number of assets, users, integrations, and verification frequency.

## Important boundary

If a percentage of asset value is used, it must be reviewed for regulatory classification before commercial launch. The product must not describe a technical audit fee as an insurance premium unless the required legal and regulatory structure exists.

## Example calculation model

For an asset value V:

    annual_service_fee = base_fee + V * rate

The rate is a commercial parameter, not a probability of loss and not a promise of recovery.

## Acceptance criteria

- pricing formula is deterministic;
- invoice amount is reproducible from recorded inputs;
- verified asset value is distinguished from declared value;
- fees are separated from any future regulated insurance premium;
- customer receives an explicit scope and limitation statement;
- no promise of protection against a specific systemic event is made without a licensed underwriting structure.

## Future regulated interface

If the product later becomes connected to actual risk transfer:

Customer -> Evidence Package -> Licensed Underwriter / Insurer -> Policy

Imperial Audit remains the evidence and verification layer unless the company obtains the permissions required for another role.
