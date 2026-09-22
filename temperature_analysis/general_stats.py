import numpy as np

from read_temperatures import load_temperatures


def main():
    data = load_temperatures()
    day = data["temperature_day_c"]
    night = data["temperature_night_c"]

    print(f"Days count: {data.size}")
    print(f"Highest day temperature: {np.max(day)}")
    print(f"Lowest night temperature: {np.min(night)}")
    print(f"Mean day temperature: {np.mean(day):.2f}")
    print(f"Mean night temperature: {np.mean(night):.2f}")
    print(f"Median day temperature: {np.median(day)}")
    print(f"Median night temperature: {np.median(night)}")
    print(f"Sum of day temperatures: {np.sum(day)}")
    print(f"Sum of night temperatures: {np.sum(night)}")


if __name__ == "__main__":
    main()
