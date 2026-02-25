# finding-e

Small experiments for approximating Euler's number `e`.

## What You Were Probably Doing (Timeline)

- **2024-09-01 11:22 (+0900)**: Created repo and wrote the first note (`"i had an idea this morning"`).
- **2024-09-01 11:48 (+0900)**: Added `main.py` (`found it`) with a stochastic search approach: tune the base `b` in `b^x` so derivative and function match, which converges toward `e`.
- **2024-09-01 11:52 (+0900)**: Added `main2.py` (`found it again`) with a series approach: summing `1/n!`, which also converges to `e`.
- **2026-02-25 11:33 (+0900)**: Started archive/modernization pass (`uv init`, moved code into `src/`).
- **2026-02-25 (later)**: Renamed scripts for clarity and finished `uv` dependency setup.

## Current Structure

- `src/derivative_search.py`: random/iterative derivative-matching experiment.
- `src/factorial_series.py`: factorial-series experiment.

These are two independent scripts (two different ways of finding `e`).

## Run (uv)

Install/sync dependencies:

```bash
uv sync
```

Run derivative search experiment:

```bash
uv run python src/derivative_search.py
```

Run factorial series experiment:

```bash
uv run python src/factorial_series.py
```

Optional flags:

```bash
uv run python src/derivative_search.py --iterations 300 --samples 16 --seed 42
uv run python src/factorial_series.py --iterations 30 --show-terms
```
