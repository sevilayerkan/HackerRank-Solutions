#!/bin/python3

import math
import os
import random
import re
import sys

def isOdd (num):
    if (num % 2 == 0):
        return 0
    else:
        return 1
    
def isWeird(n):
    if isOdd(n):
        print("Weird")
    else:
        if n <= 5:
            print("Not Weird")
        elif n <= 20:
            print("Weird")
        else:
            print("Not Weird")
            

    

if __name__ == '__main__':
    N = int(input())
    isWeird(N)
