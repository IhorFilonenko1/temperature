import numpy as np

from read_temperatures import load_temperatures

OUTPUT_FILE = "results.tsv"


def main():
    data = load_temperatures()
    day = data["temperature_day_c"]
    night = data["temperature_night_c"]

    rows = [
        ("min_night_temperature", np.min(night)),
        ("max_day_temperature", np.max(day)),
        ("mean_day_temperature", round(float(np.mean(day)), 2)),
        ("mean_night_temperature", round(float(np.mean(night)), 2)),
        ("sum_day_temperature", np.sum(day)),
        ("sum_night_temperature", np.sum(night)),
        ("days_count", data.size),
        ("below_zero_nights", np.sum(night < 0)),
        ("at_or_above_30_days", np.sum(day >= 30)),
    ]

    np.savetxt(OUTPUT_FILE, rows, fmt="%s\t%s", header="metric\tvalue", comments="")
    print(f"Results exported to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
