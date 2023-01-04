#!/bin/python3

import math
import os
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    '''
    Function returns the time difference between entered
    times from 2 different timezones.
    Input format: t1 = Day dd Mon yyyy hh:mm:ss +xxxx
    [+xxxx is timezone]
    '''
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    delta = str(int(abs((t1-t2).total_seconds())))
    return delta
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
        fptr.write(delta + '\n')
    fptr.close()
