import numpy as np

from read_temperatures import load_temperatures


def main():
    data = load_temperatures()
    day = data["temperature_day_c"]
    night = data["temperature_night_c"]
    dates = data["date"]

    coldest_idx = np.argmin(night)
    warmest_idx = np.argmax(day)

    print(f"Index of day with lowest night temperature: {coldest_idx}")
    print(f"Index of day with highest day temperature: {warmest_idx}")
    print(f"Lowest night temperature: {night[coldest_idx]} C on {dates[coldest_idx]}")
    print(f"Highest day temperature: {day[warmest_idx]} C on {dates[warmest_idx]}")


if __name__ == "__main__":
    main()
