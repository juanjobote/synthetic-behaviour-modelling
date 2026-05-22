# Synthetic Behaviour Modelling

This repository contains Python scripts, input data, and reproducible outputs associated with a study on modelling open science behaviour using a bootstrap-based Monte Carlo approach.

The project explores how synthetic data can preserve the statistical structure of behavioural datasets related to open science practices.

---

## 📌 Project Overview

The workflow includes:

- Data preprocessing and transformation
- Likert-scale encoding
- Construction of behavioural indicators
- Composite index calculation
- Bootstrap-based Monte Carlo synthetic data generation
- Statistical comparison between real and synthetic datasets
- Generation of reproducible figures and tables

The study focuses on behavioural dimensions associated with:

- Data deposit behaviour
- Data reuse
- Transparency attitudes
- Peer review perceptions
- Conflict perception

---

## 📂 Repository Structure

```text
synthetic-behaviour-modelling/

├── code/
│   └── monte_carlo_v1.py

├── data/
│   └── dataset_input.xlsx

├── output/
│   ├── figures/
│   │   ├── fig1_real.png
│   │   ├── fig2_synthetic.png
│   │   ├── fig3_attitude.png
│   │
│   ├── tables/
│   │   ├── comparison_FINAL.csv
│   │   ├── fig1_real_data_deposit.csv
│   │   ├── fig2_synthetic_data_deposit.csv
│   │   ├── fig3_open_science_attitude.csv
│
├── README.md
├── requirements.txt

## 🔁 Reproducibility

All figures included in this repository are accompanied by the underlying data used to generate them.

The repository contains the complete workflow required to reproduce the analyses, statistical comparisons, and outputs presented in the associated study.

---

## 📊 Associated Dataset

The processed datasets and scientific outputs associated with this study are publicly available via Zenodo:

👉 https://doi.org/10.5281/zenodo.20346492

The Zenodo repository includes:

- Cleaned dataset
- Synthetic dataset
- Statistical comparison dataset
- Figure datasets
- Dataset documentation

⚙️ Requirements

Install required libraries using:

pip install -r requirements.txt

Main dependencies:

pandas
numpy
matplotlib
💻 Code Description

The main script:

code/monte_carlo_v1.py

performs:

Data loading
Variable transformation
Likert-scale mapping
Composite index generation
Synthetic data generation
Statistical comparison
Figure and table export

📖 Citation

If you use this repository, please cite:

Boté-Vericad, J.-J. (2026). Synthetic Behaviour Modelling. GitHub repository.

👤 Author

Juan-José Boté-Vericad
UBICS – Universitat de Barcelona

📜 License

This repository is distributed under the MIT License.
