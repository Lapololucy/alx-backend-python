#!/usr/bin/env python3

from typing import List, Tuple

def zoom_array(lst: Tuple[int], factor: int = 2) -> Tuple[int]:
    """
    Zooms in the given tuple by repeating each element 'factor' times.

    Args:
        lst (Tuple[int]): The input tuple.
        factor (int): The factor by which each element should be repeated. Default is 2.

    Returns:
        Tuple[int]: The zoomed-in tuple with elements repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return tuple(zoomed_in)


# Test the function
array: Tuple[int] = (12,)

zoom_2x: Tuple[int] = zoom_array(array)

zoom_3x: Tuple[int] = zoom_array(array, 3)
