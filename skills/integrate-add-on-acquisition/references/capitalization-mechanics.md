# Capitalization mechanics

## Establish the ownership basis

Identify the cap table's definitions before calculating transaction activity:

- Legal entity and capitalization date
- Security classes and class-specific rights
- Authorized, issued, outstanding, vested, granted, reserved, and unallocated amounts
- Basic, as-converted, and fully diluted denominators
- Economic and voting ownership definitions
- Treatment of options, warrants, profits interests, phantom equity, convertibles, and incentive pools
- Rounding conventions and issuance precision

Do not mix counts from different dates, legal entities, security classes, or dilution definitions.

## Resolve rollover semantics

For each holder, determine whether the governing agreement defines rollover as:

- A fixed currency amount
- A percentage of gross proceeds
- A percentage of eligible or net proceeds
- Retained ownership in the acquired company
- A target percentage of the post-close combined company
- An exchange of a specified number or class of securities

Do not treat these formulations as interchangeable. Identify any excluded proceeds, fees, taxes, debt payoff, escrow, holdback, or other deductions before applying a percentage.

When the documents support a value-based issuance, calculate:

`issued units = approved contribution or rollover value / applicable issuance price`

When the documents specify an exchange ratio, calculate from the eligible surrendered securities. Apply the governing rounding rule and preserve the pre-rounding amount and residual.

If a stated post-close ownership target controls, solve only from the documented denominator and transaction sequence. Do not infer that target from a percentage stated for another purpose.

## Build the security rollforward

Roll each class and holder separately:

`pre-close securities + issuances + exercises + conversions - redemptions - cancellations - forfeitures = post-close securities`

Include distinct transaction rows for:

- Sponsor equity
- Co-investor equity
- Seller or management rollover
- Management incentive grants
- New or expanded option or incentive pool
- Warrants, convertibles, and other instruments
- Redemptions, cancellations, and converted pre-close securities

Do not count an unallocated pool as granted securities. Include it in a fully diluted denominator only when the destination definition or governing agreement requires it.

## Sequence dilution correctly

Determine whether incentive-pool creation, rollover issuance, sponsor funding, co-invest funding, conversion, and other transactions occur pre-money or post-money and in what sequence. A pool sized to a post-close percentage requires algebraic gross-up; adding a percentage of the pre-pool denominator will understate it.

For a pool intended to equal `p` of the post-pool fully diluted capitalization, with `B` securities outstanding before creating the pool:

`new pool = p * B / (1 - p)`

Use this only when the governing documents define that denominator and no other simultaneous issuance changes the equation. Otherwise solve the full documented transaction sequence.

## Calculate ownership views

Calculate each supported view from its own denominator:

`holder ownership = holder securities in view / total securities in view`

Show, when applicable:

- Basic ownership
- As-converted ownership
- Fully diluted ownership
- Voting ownership
- Economic ownership
- Sponsor, co-investor, seller, management, and employee-pool group ownership

Do not imply equal economics across classes merely because the units share a denominator. Preserve liquidation preferences, participation, conversion, vesting, hurdle, or distribution-waterfall differences in the class labels or supporting schedules.

## Protect holder data

Limit holder-level personal information to what is necessary for the cap-table calculation. Preserve source identifiers and lineage, but do not expose tax identifiers, bank information, home addresses, or unrelated personal data in the output report.
