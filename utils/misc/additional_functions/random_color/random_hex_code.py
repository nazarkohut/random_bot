"""
Contains method for hex code generation.
"""
import numpy as np


def random_hex_code() -> str:
    def generate_rgb() -> list[int]:
        return [np.random.randint(0, 255) for _ in range(3)]

    red, green, blue = generate_rgb()
    return f"{red:02X}{green:02X}{blue:02X}"
