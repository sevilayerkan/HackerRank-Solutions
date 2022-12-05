#!/bin/python3

import math
import os
import random
import re
import sys


def stringToInteger(S):
    try:
        print(int(S))
    except ValueError:
        print("Bad String")


S = input()
stringToInteger(S)
