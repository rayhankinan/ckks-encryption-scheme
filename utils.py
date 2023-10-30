import numpy as np
from typing import Any

# Rounds coordinates randonmly (Learning with Errors)


def coordinate_wise_random_rounding(coordinates: np.ndarray[Any, np.dtype[np.float64]]) -> np.ndarray[Any, np.dtype[np.int64]]:
    r = np.array(coordinates - np.floor(coordinates), dtype=np.float64)
    f = np.array(
        [
            np.random.choice([c, c - 1], 1, p=[1 - c, c])
            for c in r
        ],
        dtype=np.float64
    ).reshape(-1)

    float_rounded_coordinates = np.array(coordinates - f, dtype=np.float64)
    int_coordinates = [
        int(np.real(coeff))
        for coeff in float_rounded_coordinates
    ]

    return np.array(int_coordinates, dtype=np.int64)
