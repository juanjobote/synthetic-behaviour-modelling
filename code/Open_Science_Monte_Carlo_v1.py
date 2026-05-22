# Synthetic Behaviour Modelling using Bootstrap-Based Monte Carlo Simulation
# -------------------------------------------------------------------------
# This script performs preprocessing, variable transformation, synthetic
# data generation, and statistical comparison for modelling open science
# behaviour using survey-based data.
#
# Associated dataset:
# https://doi.org/10.5281/zenodo.20346492
#
# Repository:
# https://github.com/juanjobote/synthetic-behaviour-modelling
#
# Main components:
# - Data cleaning and transformation
# - Likert-scale encoding
# - Composite index construction
# - Bootstrap-based Monte Carlo synthetic data generation
# - Statistical comparison between real and synthetic datasets
# - Figure and table generation
#
# Author: Juan-José Boté-Vericad
# Affiliation: UBICS – Universitat de Barcelona
# Repository: synthetic-behaviour-modelling
# Version: v1.0
# Year: May 2026

# Correct execution with proper ordering and export

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load
# Path placeholder — dataset available via Zenodo
BASE_DIR = Path(__file__).resolve().parent.parent

data_path = BASE_DIR / "data" / "dataset_input.xlsx"

df = pd.read_excel(data_path)
df.columns = df.columns.str.upper()

# Mapping FIRST
df["A1_DATA_DEPOSIT"] = df["A1_DATA_DEPOSIT"].replace({
    "Sí": 2,
    "No": 0,
    "No, pero lo haré en un futuro a corto o medio plazo": 1
})

df["A2_DATA_REUSE"] = df["A2_DATA_REUSE"].replace({
    "Sí": 1,
    "No": 0,
    "No lo sé": np.nan,
    "NA": np.nan
})

likert_map = {
    "Está muy en desacuerdo": 1,
    "Está en desacuerdo": 2,
    "No está de acuerdo": 2,
    "No está en absoluto de acuerdo": 1,
    "No está ni de acuerdo ni en desacuerdo": 3,
    "Está de acuerdo": 4,
    "Está muy de acuerdo": 5,
    "N/A": np.nan
}

likert_cols = [
    "D1_TRANSPARENCY_ATTITUDE",
    "D2_REVIEW_QUALITY_ATTITUDE",
    "D3_CONFLICT_INV"
]

#for col in likert_cols:
#   df[col] = df[col].replace(likert_map)
df[likert_cols] = df[likert_cols].replace(likert_map)

#todo es bien mapeado?
print(df["D1_TRANSPARENCY_ATTITUDE"].unique())

# Convert AFTER mapping
all_cols = [
    "A1_DATA_DEPOSIT",
    "A2_DATA_REUSE",
    "D1_TRANSPARENCY_ATTITUDE",
    "D2_REVIEW_QUALITY_ATTITUDE",
    "D3_CONFLICT_INV"
]

df[all_cols] = df[all_cols].apply(pd.to_numeric, errors="coerce")


df["D3_CONFLICT_INV"] = 6 - df["D3_CONFLICT_INV"]

print(df[all_cols].describe())

#Minimal validation to avoid errors
print("\nMissing values per column:")
print(df[likert_cols].isna().sum())

#ensuring the mapping is right
print("\nMin/Max values:")
for col in likert_cols:
    print(col, df[col].min(), df[col].max())

# Composite
cols = [
    "D1_TRANSPARENCY_ATTITUDE",
    "D2_REVIEW_QUALITY_ATTITUDE",
    "D3_CONFLICT_INV"
]


# Calcular índice
df["OPEN_SCIENCE_ATTITUDE"] = df[cols].mean(axis=1).round(3)


# Monte Carlo
df_synth = df.sample(n=300, replace=True, random_state=42)

# Comparison
comparison = pd.DataFrame({
    "VARIABLE": cols + ["OPEN_SCIENCE_ATTITUDE"],
    "REAL_MEAN": df[cols + ["OPEN_SCIENCE_ATTITUDE"]].mean().values,
    "SYNTHETIC_MEAN": df_synth[cols + ["OPEN_SCIENCE_ATTITUDE"]].mean().values
})

comparison = comparison.round(3)

# Plots
#Figure 1
plt.figure()
df["A1_DATA_DEPOSIT"].value_counts().sort_index().plot(kind="bar")
plt.title("Real Data - Data Deposit")
# Figure 1 data generation
fig1_data = df["A1_DATA_DEPOSIT"].value_counts().sort_index()
fig1_data.to_csv("fig1_real_data_deposit.csv")
#tiff generation
plt.savefig("fig1.png", dpi=300, bbox_inches="tight")
plt.savefig("fig1.tiff", dpi=300, bbox_inches="tight",  pil_kwargs={"compression": "tiff_lzw"})
plt.show()


#Figure 2
plt.figure()
df_synth["A1_DATA_DEPOSIT"].value_counts().sort_index().plot(kind="bar")
plt.title("Synthetic Data - Data Deposit")
# Figure 2 data generation
fig2_data = df_synth["A1_DATA_DEPOSIT"].value_counts().sort_index()
fig2_data.to_csv("fig2_synthetic_data_deposit.csv")
#tiff generation
plt.savefig("fig2.png", dpi=300, bbox_inches="tight")
plt.savefig("fig2.tiff", dpi=300, bbox_inches="tight",  pil_kwargs={"compression": "tiff_lzw"})
plt.show()

#figure 3 
plt.figure()
df["OPEN_SCIENCE_ATTITUDE"].hist()
plt.title("Open Science Attitude")
# Figure 3 data generation
fig3_data = df["OPEN_SCIENCE_ATTITUDE"].value_counts().sort_index()
fig3_data.to_csv("fig3_open_science_attitude.csv")
plt.savefig("fig3.png", dpi=300, bbox_inches="tight")
plt.savefig("fig3.tiff", dpi=300, bbox_inches="tight",  pil_kwargs={"compression": "tiff_lzw"})
plt.show()


# Save files
#df.to_csv("dataset_FIXED_correct.csv", index=False)
#df_synth.to_csv("synthetic_FIXED_correct.csv", index=False)
#comparison.to_csv("comparison_FINAL.csv", index=False)

df.to_csv("C:/congreso_iscaf/dataset_FIXED_correct.csv", index=False)
df_synth.to_csv("C:/congreso_iscaf/synthetic_FIXED_correct.csv", index=False)
comparison.to_csv("C:/congreso_iscaf/comparison_FINAL.csv", index=False)

