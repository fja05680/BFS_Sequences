#!/usr/bin/env python
# coding: utf-8

# Write a computer program that implements the Box-Muller method

# use future imports for python 3.x forward compatibility
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# other imports
import math

# project imports
import rand
import halton
import bfs

# Write a computer program that implements the Box-Muller method
#
# Box-Muller: pseudorandom
# 1. Generate random $u_1$ , $u_2$ independently from U(0, 1)
# 2. Compute: $R^2$ = $−2\,log\,u_1$ and $θ = 2π\,u_2$
# 3. $X = R\,cos\,θ$
# $Y = R\,sin\,θ$

def box_muller(u1, u2):

    r = -2 * math.log(u1)
    r = math.sqrt(r)
    theta = 2 * math.pi * u2

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    return x, y

def box_muller_seq(s, N, seq=rand.rand_seq):
    ''' return a list of N standard normal vectors (tuples) of dimension s '''

    # save the original values for use later
    s_orig = s
    N_orig = N

    # both s and N should be even
    N = N if N % 2 == 0 else N + 1
    s = s if s % 2 == 0 else s + 1

    sns = []
    rows = seq(s, N)
    for row in rows:
        snv = []
        for i in range(0, len(row), 2):
            x, y = box_muller(row[i], row[i+1])
            snv.append(x); snv.append(y)

        # resize vector to original dimension s and add to sns list
        sns.append(tuple(snv[:s_orig]))

    return sns[:N_orig]


#sn = box_muller_seq(s=2, N=10, seq=rand.rand_seq)
#print(sn[:10])

