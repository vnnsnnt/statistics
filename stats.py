import numpy as np 
import statistics
import matplotlib.pyplot as plt 

def fivenum(data):
    """FIVE NUMBER SUMMARY"""
    return np.percentile(data, [0, 25, 50, 75, 100], interpolation="midpoint")

def getCount(data, min=0, max=0, intervals=[]):
    total = 0 
    if len(intervals) < 1:
        for i in data:
            if i < max:
                if i >= min: 
                    total += 1 
        return total
    else:
        for i in range(0, len(intervals), 2):
            for j in data: 
                if j < intervals[i+1]:
                    if j >= intervals[i]: 
                        total += 1 
            print("For", intervals[i], "to", intervals[i+1], ":", total)
            total = 0
                    
from numpy import mean, absolute 

def absMean(data):
    print("Sample Mean Value =", mean(data)) 
    sum = 0 
    M = mean(data)
    for i in range(len(data)): 
        dev = absolute(data[i] - M) 
        sum += dev 
    print("Mean Absolute Deviation:", sum/len(data)) 





