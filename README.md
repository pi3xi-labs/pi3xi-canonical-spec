# Pi³XI Canonical Spec

> Pi³XI: An observation-record invariant framework.

The Pi³XI model separates observation, interpretation, execution, and governance into distinct layers. The objective is to preserve invariants while allowing coordinates, implementations, and runtime details to evolve.

## Status

- **Status:** Public Canonical Specification
- **Reference Contract:** Sentinel Observation Contract `contracts-v1.3`

## Core Principles

### 1. Coordinate Invariance

Coordinates may change. Invariants must be preserved.

座標は変えてもよいが、不変量は保存する。

See [`principles/coordinate-invariant.md`](principles/coordinate-invariant.md).

### 2. Observation First

Record observations, not explanations.

説明ではなく観測結果を記録する。

See [`principles/observation-first.md`](principles/observation-first.md).

### 3. Responsibility Boundaries

Intent, Event, Observe, and Meta are separate responsibilities.

| Layer   | Responsibility                     |
|---------|------------------------------------|
| Intent  | Desired action                     |
| Event   | State transition                   |
| Observe | Observable result                  |
| Meta    | Audit and governance metadata      |

See [`principles/responsibility-boundaries.md`](principles/responsibility-boundaries.md).

## Canonical Invariants

### Phase 1

Invariant vector:

```
I = (d_KG, d_GF, d_KF)
```

Protected property: **SO(2) rotational invariance**.

### Future Expansion

Future phases may add `d_W` and `d_M` without invalidating Phase 1.

See [`invariants/phase1-invariants.md`](invariants/phase1-invariants.md) and [`invariants/metric-definitions.md`](invariants/metric-definitions.md).

## Runtime Model

The runtime is organized around the **Canonical Record**.

```
Intent
  ↓
Event
  ↓
Observe
  ↓
Meta
```

Implementations may vary. Canonical Records must remain auditable.

See [`runtime/`](runtime/).

## Repository Layout

```
README.md
GOVERNANCE.md
LICENSE
principles/
  coordinate-invariant.md
  observation-first.md
  responsibility-boundaries.md
invariants/
  phase1-invariants.md
  metric-definitions.md
runtime/
  canonical-record.md
  intent-event-observe-meta.md
  observation-interface.md
contracts/
  references.md
releases/
  spec-v1.0.md
tools/
  validate_spec.py
.github/workflows/
  spec-check.yml
```

## Related Repositories

- **Canonical contract:** [pi3xi-labs/sentinel-observation-contract](https://github.com/pi3xi-labs/sentinel-observation-contract)
- **Operational repository:** [wizyig/gbox](https://github.com/wizyig/gbox)

See [`contracts/references.md`](contracts/references.md).

## Governance

See [`GOVERNANCE.md`](GOVERNANCE.md).

## Contributing

Contributions are welcome.

Before submitting a change, run:

```
python tools/validate_spec.py
```

- Protected invariants must not change without governance review.
- Breaking changes require a major-version proposal.

Origin: Structure Lock (contracts-v1.0) was frozen in the operational repo `wizyig/gbox` at `823515c81fc234f36e2e372e0a00d140b901714e` before extraction to this canonical repository.

## License

[CC0 1.0 Universal](LICENSE)

