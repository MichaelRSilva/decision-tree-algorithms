import csv
from typing import Tuple

import numpy as np

from config import dataset_path


def read_data() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    content = np.loadtxt(dataset_path, delimiter=',', skiprows=1)

    with open(dataset_path) as f:
        reader = csv.reader(f)
        header = next(reader)

    return content[:, :-1], content[:, -1], header
