# Project Guide

## Purpose and layout

- This is a beginner data-analysis project for DataCorp, with French-language labels and identifiers.
- `data/sales.csv` contains sales rows with `id` and `montant` columns. The sample includes positive, zero, and negative amounts.
- `src/stats_utils.py` is the current analysis script and uses pandas and NumPy.
- `README.md` and `notes.txt` are brief onboarding and learning notes.

## Working conventions

- Preserve the project's French naming and output style when extending its analysis.
- Keep CSV input paths relative to the repository root unless the project is deliberately made location-independent.
- Treat `montant <= 0` as invalid only where the analysis explicitly requires that rule; do not silently alter source data.
- No dependency manifest or automated test suite is currently present. Do not assume one exists or introduce a framework for a small change without need.
- The current script is exploratory, not a verified working entry point: `analyser_ventes` uses DataFrame operations but is called with an empty list. Check the expected input type and run path before relying on its output.
