# Lab 1: Reproducible Computing Setup

This repository contains my Lab 1 project for reproducible computing. The project uses Python and a conda environment to read a small CSV dataset and calculate a simple summary statistic.

## Project Structure

```text
lab1-reproducible-setup/
├── README.md
├── AI_USAGE.md
├── .gitignore
├── environment.yml
├── src/
│   └── analysis.py
└── data/
    └── example.csv
```

## Setup

This project requires Anaconda, Miniconda, or another installation of conda.

Clone the repository:

```bash
git clone https://github.com/mariumkalhoro11/lab1-reproducible-setup.git
cd lab1-reproducible-setup
```

Create the conda environment:

```bash
conda env create -f environment.yml
```

Activate the environment:

```bash
conda activate lab1
```

## Run the Analysis

Run the analysis script with:

```bash
python src/analysis.py
```

The script reads `data/example.csv` and produces output similar to:

```text
Lab 1 analysis ran successfully.
Rows: 5
Mean value: 30.00
```

## Reproducibility

The environment is defined in `environment.yml`. To verify reproducibility, the environment can be deleted and recreated using only this file before running the analysis again.

```bash
conda env remove -n lab1 -y
conda env create -f environment.yml
conda activate lab1
python src/analysis.py
```
