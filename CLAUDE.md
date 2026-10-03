# CLAUDE.md

## Purpose
Study repo for *Engineering Design Optimization* (Martins & Ning), about 4 h/week, drone-oriented.
Fork of github.com/mdobook/resources (`upstream`), published as github.com/S0mar/MDO_Learn (`origin`).
The goal is learning: the owner works the end-of-chapter problems in Python (NumPy/SciPy/Matplotlib, later JAX and OpenMDAO) and builds their own reusable optimizer package, `mdolib`.

## Environment
```
mamba activate mdo      # Python 3.12; spec in environment.yml
```
Jupyter kernel: "Python (mdo)". `mdolib` is installed editable (`pip install -e .`).
Checks: `pytest -q` and `ruff check mdolib tests`.

## Layout
```
mdolib/            # my optimization library (grows as the book progresses)
solutions/         # my work, one folder per chapter (solutions/ch01/ ...)
solutions/README.md  # status table: Ch | Core problems | Status
tests/             # pytest tests for mdolib (+ smoke test)
environment.yml    # conda env "mdo"
pyproject.toml     # mdolib packaging (setuptools)
exercises/         # authors' original code (read-only, see rules)
```

## Rules
- Never write solutions to book problems unless the owner explicitly asks. Do not implement optimization algorithms unprompted. Scaffolding, templates and tooling are fine.
- When asked to review work, check: (1) correctness, (2) verification (compare against SciPy; check gradients with finite differences or complex step), (3) interpretation of the results.
- Never modify the authors' original folders (`exercises/` etc.). Load them as-is (e.g. via importlib) if needed.
- Never touch `~/projects/aersoSimV1` or the `aero-opt` conda env.
