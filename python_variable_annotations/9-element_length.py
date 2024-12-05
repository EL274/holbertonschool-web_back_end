#!/usr/bin/python3
from typing import list, tuple

def element_length(lst: list[str]) -> list[tuple:(str, int)] :

    return [(i, len(i))for i in lst]
