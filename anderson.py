#!/usr/bin/env python
# coding: utf-8

# Anderson Darling

# imports
import math
import numpy
import random


def _phi(x):
    'Cumulative distribution function for the standard normal distribution'
    return (1.0 + math.erf(x / math.sqrt(2.0))) / 2.0

def anderson_darling(x, mean=None):

    x = numpy.array(x)
    x = sorted(x)
    if mean is None:
        mean = numpy.mean(x)
    var = numpy.var(x)
    std = numpy.std(x)
    N = len(x)

    y = [(xi - mean)/std for xi in x]
    # start list at index 1
    y = [None] + y

    A = 0
    for i in range(1, N+1):
        A += (2*i - 1)*(math.log(_phi(y[i])) + math.log(1 - _phi(y[N+1-i])))
    A = -N - 1/N * A

    return A


# Statistic:
# 10.00: 1.760
# 5.000: 2.323
# 2.500: 2.904
# 1.000: 3.690

