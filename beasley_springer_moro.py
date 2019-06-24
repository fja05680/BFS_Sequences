#!/usr/bin/env python
# coding: utf-8

# Write a computer program that implements the Beasley-Springer-Moro algorithm

# use future imports for python 3.x forward compatibility
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# other imports
import math
import random

# project imports
import rand
import halton
import bfs


# Write a computer program that implements the Beasley-Springer-Moro algorithm
#
# Pseducode for the Beasley-Springer-Moro Algorithm:
# <img src="./moro.jpg" alt="moro" align="left" width="480"/>
#

def beasley_springer_moro(u):
    ''' input:  u between 0 and 1
        output: x, approximation to inverse normal
    '''

    x = 0

    # constants needed for algorithm
    a0 =      2.50662823884;   b0 =     -8.47351093090
    a1 =    -18.61500062529;   b1 =     23.08336743743
    a2 =     41.39119773534;   b2 =    -21.06224101826
    a3 =    -25.44106049637;   b3 =      3.13082909833

    c0 = 0.3374754822726147;   c5 = 0.0003951896511919
    c1 = 0.9761690190917186;   c6 = 0.0000321767881768
    c2 = 0.1607979714918209;   c7 = 0.0000002888167364
    c3 = 0.0276438810333863;   c8 = 0.0000003960315187
    c4 = 0.0038405729373609;

    y = u - 0.5
    if abs(y) < 0.42:
        r = y * y
        x = y * (((a3 * r + a2) * r + a1) * r + a0)/ \
               ((((b3 * r + b2) * r + b1) * r + b0) * r + 1.0)
    else:
        r = u
        if (y > 0): r = 1 - u
        r = math.log(-math.log(r))
        x = c0 + r * (c1 + r * (c2 + r * (c3 + r * (c4 + \
            r * (c5 + r * (c6 + r * (c7 + r * c8)))))))
        if (y < 0): x = -x

    return x

def beasley_springer_moro_seq(s, N, seq=rand.rand_seq):
    ''' return a list of N standard normal vectors (tuples) of dimension s '''

    sns = []
    rows = seq(s, N)
    for row in rows:
        snv = [beasley_springer_moro(col) for col in row]
        sns.append(tuple(snv))

    return sns

#test
#sns = beasley_springer_moro_seq(s=2, N=1000, seq=bfs.bfs_seq)
#print(len(sns))
#print(sns[:10])

