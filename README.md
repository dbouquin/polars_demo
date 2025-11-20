# Time Series Analysis with Polars: Exoplanet Transit Detection

A beginner-friendly tutorial that teaches Polars (a modern, fast data manipulation library) by analyzing real NASA space telescope data to detect an exoplanet transit.

## What You'll Learn

- Load and explore data using Polars' eager and lazy modes
- Write Polars expressions and chain operations together
- Understand when and why to use lazy evaluation for query optimization
- Handle missing data and create derived columns
- Perform time series operations (rolling windows, binning, grouping)
- Compare Polars and pandas performance on real tasks
- Create both static (matplotlib) and interactive (Bokeh) visualizations

## What We're Analyzing

This tutorial uses real observational data from NASA's TESS (Transiting Exoplanet Survey Satellite) mission. We'll analyze a phase-folded light curve from the hot Jupiter exoplanet **WASP-18 b** to:
- Detect the transit signal (when the planet passes in front of its star)
- Measure the transit depth (observed brightness decrease caused by the transit)
- Calculate transit properties
- Create beautiful visualizations of the light curve

## Prerequisites

**You should be comfortable with:**
- Python basics (functions, loops, variables)
- DataFrame concepts (rows, columns, filtering, grouping)
- Basic pandas (if you've used `df[df['col'] > 5]`, you're good!)

**You do NOT need:**
- Deep pandas expertise
- Prior Polars experience
- Astronomy knowledge (we explain everything!)

## Getting Started

### 1. Clone (or download) this repository

```bash
git clone git@github.com:dbouquin/polars_demo.git
cd polars-timeseries-tutorial
```

### 2. Create a conda environment

We recommend using conda to manage your Python environment and dependencies:

```bash
# Create a new conda environment named 'polars-tutorial' 
conda create -n polars-tutorial python=3.13 -y

# Activate the environment
conda activate polars-tutorial
```

### 3. Install required packages

Install all necessary packages using conda:

```bash
conda install -c conda-forge polars pandas numpy matplotlib bokeh pyarrow -y
```

### 4. Download the data

The tutorial uses the CSV file in this repository called `wasp18b_lightcurve.csv`, which contains WASP-18 b light curve data. You can use this file or build your own using `fetch_data.py`:

```bash
python fetch_data.py
```

### 5. Execute the notebook
Open run `polars_timeseries_tutorial.ipynb` using your polars_tutorial environment


## Repository Structure

```
polars-timeseries-tutorial/
├── README.md                          # This file
├── polars_timeseries_tutorial.ipynb   # Main tutorial notebook
├── wasp18b_lightcurve.csv             # Light curve data 
└── fetch_data.py                      # Script to download data (optional)
```

## Acknowledgements

- Built with Polars, pandas, matplotlib, Bokeh
- Data fetch and plotting adapted from STScI Archive Scientist Susan Mullally's [Exoplanet Data and TESS Light Curves Using Python Requests](https://spacetelescope.github.io/mast_notebooks/notebooks/TESS/beginner_tess_exomast/beginner_tess_exomast.html)
- Tutorial developed for the Anaconda community