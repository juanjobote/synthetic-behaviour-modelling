# Synthetic Behaviour Modelling — v2.0

Companion code for the paper:

> Boté-Vericad, J.-J. (2026). *Modelling Open Science Behaviour Using Synthetic
> Data with a Monte Carlo Approach*. ICAISF 2026.

This release accompanies the peer-reviewed camera-ready version of the paper.

## Version history

- **v1.0** — Initial release. Bootstrap-based Monte Carlo synthesis with
  M = 300 and comparison of means across three attitudinal variables and the
  composite Open Science Attitude index.
- **v2.0** — Current release. Extends v1.0 with:
  - Cronbach's α reported for the composite attitude index (α = 0.675).
  - Extended synthetic sample size (M = 500).
  - B = 1000 bootstrap replicates for 95% percentile confidence intervals.
  - Kolmogorov–Smirnov two-sample tests for distributional equivalence.
  - Chi-square tests of independence for categorical variables.
  - Spearman rank correlation matrices (real vs synthetic).
  - Frequency comparison by data-deposit category.
  - Fully reproducible workflow with fixed random seed (seed = 42) and
    self-contained relative paths.

Substantive findings are unchanged; methodological validation is
strengthened following peer review.

## Repository structure

```
synthetic-behaviour-modelling-v2.0/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── code/
│   └── Open_Science_Monte_Carlo_v2.py
├── data/
│   └── dataset_input.xlsx
└── output/
    ├── figures/
    │   ├── Fig1_attitude.tiff
    │   └── Fig1_attitude.png
    └── tables/
        ├── descriptive_stats.csv
        ├── fidelity_tests.csv
        ├── deposit_frequencies.csv
        ├── spearman_correlations.csv
        ├── dataset_real_processed.csv
        └── dataset_synthetic.csv
```

## How to reproduce

Requires Python 3.9 or later.

```bash
# From the project root
pip install -r requirements.txt
python code/Open_Science_Monte_Carlo_v2.py
```

Outputs are written to `output/figures/` and `output/tables/`.
Because the random seed is fixed to 42, running the script produces
byte-identical numerical results across runs and environments.

## Data

The input file `data/dataset_input.xlsx` is derived from the publicly available
survey dataset by Ollé-Castellà et al. (2023), *"Dataset sobre hábitos y
percepciones sobre la ciencia abierta de investigadores de instituciones
españolas"*, CORA — Repositori de Dades de Recerca,
DOI: [10.34810/DATA690](https://doi.org/10.34810/DATA690).

## Associated dataset release

Processed real and synthetic datasets and the derived tables are also
available as a separate Zenodo record:
[10.5281/zenodo.21324577](https://doi.org/10.5281/zenodo.21324577)
(v2.0 corresponds to the camera-ready version of the paper).

## Citation

If you use this code, please cite:

Boté-Vericad, J.-J. (2026). *Open Science Behaviour Modelling — Release
V2.0* [Software]. Zenodo. https://doi.org/10.5281/zenodo.20346970

## Contact

Juan-José Boté-Vericad — UBICS, Universitat de Barcelona
juanjo.botev@ub.edu

## License

See `LICENSE`.


This repository is distributed under the MIT License.
