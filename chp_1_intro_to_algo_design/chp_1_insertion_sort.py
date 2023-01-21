#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from typing import List


def insertion_sort(arr: List[int]) -> List[int]:
    """
    A sorting algorithm that compares two values at a time and
    switches their position with the input array

    args:
    arr -- unsorted input list
    """
    i: int = len(arr)

    for num in range(i):
        j: int = num
        while j > 0 and (arr[j] < arr[j - 1]):
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1

    return arr


if __name__ == "__main__":
    print(insertion_sort([33, 55, 32, 4, 7, 1, 9, 1999]))
