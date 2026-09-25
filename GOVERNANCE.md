# Governance

## Purpose

This document defines how the Pi³XI Canonical Spec is governed: how its principles and invariants are protected, how changes are proposed and accepted, and how releases are named.

The Canonical Spec is the parent specification. Derived contracts, such as the Sentinel Observation Contract, derive from it.

## Lock Levels

Lock levels describe progressively stronger guarantees applied to a specification or contract.

| Lock Level         | Meaning                                                                 |
|--------------------|-------------------------------------------------------------------------|
| Structure          | Required files and document structure are fixed and checked.            |
| Behavior           | Expected behavior is fixed and checked.                                 |
| Integrity          | Content integrity is fixed and verifiable.                              |
| Signature          | Released artifacts are signed and the signatures are verifiable.        |
| Contract Evolution | Rules for evolving a locked contract across versions are defined.       |

In this spec repository, only **Structure Lock** is enforced by CI at `spec-v1.0` (see `tools/validate_spec.py` and `.github/workflows/spec-check.yml`).

Higher lock levels are applied in derived contract repositories. The Sentinel Observation Contract reached **Signature Lock** at `contracts-v1.3`.

## Compatibility Principle

Higher lock levels must satisfy all lower ones.

```
Structure
  ↓
Behavior
  ↓
Integrity
  ↓
Signature
  ↓
Contract Evolution
```

## Release Naming

Release titles use the format:

```
<tag> — <title>
```

Examples for this repository:

```
spec-v1.0 — Initial Canonical Spec
```

Examples from the derived contract repository:

```
contracts-v1.0 — Structure Lock
contracts-v1.1 — Behavior Lock
contracts-v1.2 — Integrity Lock
contracts-v1.3 — Signature Lock
```

Release titles are descriptive only. Validity is determined by the tag, the commit hash, and (where present) manifest and signature artifacts.

Spec tags must match the format `spec-vMAJOR.MINOR` (regular expression `^spec-v[0-9]+\.[0-9]+$`).

## Change Process

- Changes to principles or invariants require governance review.
- Breaking changes are made only in major versions.
- All changes must pass `python tools/validate_spec.py`.
