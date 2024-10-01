"""coordinates"""

__author__ = "730753141"


def get_coords(xs: str, ys: str) -> None:
    """print the formatted pairs of each char"""
    idx1: int = 0

    while idx1 < len(xs):
        idx2: int = 0
        while idx2 < len(ys):
            print(f"({xs[idx1]},{ys[idx2]})")
            idx2 += 1
        idx1 += 1


if __name__ == "__main__":
    print(get_coords("hi", "bye"))
