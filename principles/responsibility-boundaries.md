# Responsibility Boundaries

## Principle

Intent, Event, Observe, and Meta are separate responsibilities. Each layer has a single responsibility and must not take over the responsibility of another layer.

| Layer   | Responsibility                |
|---------|-------------------------------|
| Intent  | Desired action                |
| Event   | State transition              |
| Observe | Observable result             |
| Meta    | Audit and governance metadata |

## Flow

See [`../runtime/intent-event-observe-meta.md`](../runtime/intent-event-observe-meta.md).

## Details

To be specified in a later spec release.
