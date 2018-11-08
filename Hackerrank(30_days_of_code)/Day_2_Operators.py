#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    result = meal_cost + float((tip_percent*meal_cost)/100) + float((tax_percent*meal_cost)/100)
    totalCost= int(round(result,0))
    print(totalCost)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)

