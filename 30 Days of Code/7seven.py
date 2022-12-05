#!/bin/python3

import math
import os
import random
import re
import sys

def printReverse(arr):
    print(*arr[::-1], sep=' ')
        

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
printReverse(arr)