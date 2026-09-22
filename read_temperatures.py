import numpy as np

DATA_FILE = "temperatures.csv"


def load_temperatures(file_path=DATA_FILE):
    return np.genfromtxt(
        file_path,
        delimiter=",",
        names=True,
        dtype=None,
        encoding="utf-8-sig",
    )


if __name__ == "__main__":
    data = load_temperatures()
    print("Column headers:", data.dtype.names)
    print(data)
