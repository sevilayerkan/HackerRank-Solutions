#!/bin/python3

import math
import os
import random
import re
import sys

# Takes integer and return its binary equivalent in string form


def decimalToBinary(num):
    return bin(num).replace("0b", "")

# Finds maximum number of consecutive 1's in string


def findOnes(binary):
   return (len(list(max(binary.split("0")))))


if __name__ == '__main__':
    n = int(input().strip())

    print(findOnes(decimalToBinary(n)))
