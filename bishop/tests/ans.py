from typing import Tuple

def moveBishop(starting: Tuple[int, int], target: Tuple[int, int]) -> bool:
    return abs(starting[0] - target[0]) == abs(starting[1] - target[1])
    