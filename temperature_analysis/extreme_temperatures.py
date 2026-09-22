import numpy as np

from read_temperatures import load_temperatures


def print_days(title, rows):
    print(title)
    for row in rows:
        print(f"  {row['date']}: day {row['temperature_day_c']} C, night {row['temperature_night_c']} C")
    print(f"  total: {rows.size}")


def main():
    data = load_temperatures()
    day = data["temperature_day_c"]
    night = data["temperature_night_c"]

    print_days("Days with day temperature 30 C or higher:", data[day >= 30])
    print_days("Days with night temperature below -3 C:", data[night < -3])
    print_days("Days with day temperature 25 C or higher:", data[day >= 25])
    print_days("Days with night temperature from -1 C to 1 C:", data[(night >= -1) & (night <= 1)])


if __name__ == "__main__":
    main()
