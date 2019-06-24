#!/usr/bin/env python
# coding: utf-8

# random sequence

# use future imports for python 3.x forward compatibility
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# other imports
import random


# rand_seq function
def rand_seq(s, N):
    ''' return a list of N random vectors (tuples) of dimension s '''

    rs = []
    r = random.random
    for i in range(N):
        rv = [(r()) for j in range(s)]
        rs.append(tuple(rv))
    return rs

#test
#rs = rand_seq(s=1, N=100)
#print(rs[:10])
