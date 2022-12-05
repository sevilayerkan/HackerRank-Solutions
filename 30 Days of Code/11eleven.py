#!/bin/python3

import math
import os
import random
import re
import sys


def sub_arr_sum(arr):
    return sum(arr[0]) + arr[1][1] + sum(arr[2])


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(max([sub_arr_sum([row[j: j+3] for row in arr[i: i+3]])
          for j in range(4) for i in range(4)]))
