#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
sum1=-999999
for i in range(6):
    for j in range(6):
        if (j+2 < 6 and i+2 < 6):
            sum2= (arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
            if(sum2>sum1):
                sum1=sum2
print(sum1)


