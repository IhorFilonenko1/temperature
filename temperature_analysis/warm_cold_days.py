import numpy as np

from read_temperatures import load_temperatures


def main():
    data = load_temperatures()
    day = data["temperature_day_c"]
    night = data["temperature_night_c"]

    print(f"Days with night temperature below 0 C: {np.sum(night < 0)}")
    print(f"Days with day temperature 0-9 C: {np.sum((day >= 0) & (day <= 9))}")
    print(f"Days with day temperature 10-19 C: {np.sum((day >= 10) & (day <= 19))}")
    print(f"Days with day temperature 20-29 C: {np.sum((day >= 20) & (day <= 29))}")
    print(f"Days with day temperature 30+ C: {np.sum(day >= 30)}")


if __name__ == "__main__":
    main()
