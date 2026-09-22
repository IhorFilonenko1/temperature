# Temperature Analysis

Python project for analyzing yearly temperature data with NumPy.

## Setup

```
pip install -r requirements.txt
```

## Structure

- `temperatures.csv` — daily day/night temperatures for 2025
- `read_temperatures.py` — reads the CSV into a NumPy structured array
- `temperature_analysis/` — analysis package:
  - `general_stats.py` — general statistics (min, max, mean, median, sums)
  - `coldest_warmest_day.py` — coldest night and hottest day
  - `warm_cold_days.py` — counts of days in temperature ranges
  - `extreme_temperatures.py` — lists of days with extreme temperatures
- `export_tsv.py` — exports summary metrics to `results.tsv`

## Usage

```
python read_temperatures.py
python -m temperature_analysis.general_stats
python -m temperature_analysis.coldest_warmest_day
python -m temperature_analysis.warm_cold_days
python -m temperature_analysis.extreme_temperatures
python export_tsv.py
```
