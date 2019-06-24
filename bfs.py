#!/usr/bin/env python
# coding: utf-8

# BFS sequence

# use future imports for python 3.x forward compatibility
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

# other imports
import random
import math
import numpy

# project imports
import rand


# the sX() functions build a matrix that represents a hypercube
# or a hyperrectangle, or in the case s=1, just a list of numbers

def _xlen(Xs):
    return [len(x) for x in Xs];

def _s1(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],)
             for x0 in Xs[0]]

def _s2(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1])
             for x0 in Xs[0]     for x1 in Xs[1]]

def _s3(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]]

def _s4(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]]

def _s5(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
            (x3+rand())/n[3],    (x4+rand())/n[4])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]]

def _s6(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]]

def _s7(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]]

def _s8(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]]

def _s9(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7],   (x8+rand())/n[8])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]     for x8 in Xs[8]]

def _s10(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
            (x3+rand())/n[3],    (x4+rand())/n[4],   (x5+rand())/n[5],
            (x6+rand())/n[6],    (x7+rand())/n[7],   (x8+rand())/n[8],
            (x9+rand())/n[9])
            for x0 in Xs[0]      for x1 in Xs[1]     for x2 in Xs[2]
            for x3 in Xs[3]      for x4 in Xs[4]     for x5 in Xs[5]
            for x6 in Xs[6]      for x7 in Xs[7]     for x8 in Xs[8]
            for x9 in Xs[9]]

def _s11(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7],   (x8+rand())/n[8],
             (x9+rand())/n[9],   (x10+rand())/n[10])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]     for x8 in Xs[8]
             for x9 in Xs[9]     for x10 in Xs[10]]

def _s12(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7],   (x8+rand())/n[8],
             (x9+rand())/n[9],   (x10+rand())/n[10], (x11+rand())/n[11])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]     for x8 in Xs[8]
             for x9 in Xs[9]     for x10 in Xs[10]   for x11 in Xs[11]]

def _s13(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7],   (x8+rand())/n[8],
             (x9+rand())/n[9],   (x10+rand())/n[10], (x11+rand())/n[11],
             (x12+rand())/n[12])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]     for x8 in Xs[8]
             for x9 in Xs[9]     for x10 in Xs[10]   for x11 in Xs[11]
             for x12 in Xs[12]]

def _s14(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7],   (x8+rand())/n[8],
             (x9+rand())/n[9],   (x10+rand())/n[10], (x11+rand())/n[11],
             (x12+rand())/n[12], (x13+rand())/n[13])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]     for x8 in Xs[8]
             for x9 in Xs[9]     for x10 in Xs[10]   for x11 in Xs[11]
             for x12 in Xs[12]   for x13 in Xs[13]]

def _s15(Xs):
    rand = random.random
    n = _xlen(Xs); print(n)
    return [((x0+rand())/n[0],   (x1+rand())/n[1],   (x2+rand())/n[2],
             (x3+rand())/n[3],   (x4+rand())/n[4],   (x5+rand())/n[5],
             (x6+rand())/n[6],   (x7+rand())/n[7],   (x8+rand())/n[8],
             (x9+rand())/n[9],   (x10+rand())/n[10], (x11+rand())/n[11],
             (x12+rand())/n[12], (x13+rand())/n[13], (x14+rand())/n[14])
             for x0 in Xs[0]     for x1 in Xs[1]     for x2 in Xs[2]
             for x3 in Xs[3]     for x4 in Xs[4]     for x5 in Xs[5]
             for x6 in Xs[6]     for x7 in Xs[7]     for x8 in Xs[8]
             for x9 in Xs[9]     for x10 in Xs[10]   for x11 in Xs[11]
             for x12 in Xs[12]   for x13 in Xs[13]   for x14 in Xs[14]]

def bfs_seq(s, N, hyper_rect=True, shuffle=True, exact_N=True):
    ''' return a list of N bfs vectors (tuples) of dimension s '''

    # calculate number of partitons per dim
    n = N**(1/s)
    print('partitions per dimension = {:.02f}'.format(n))

    # for dim 1, some options are invalid, so turn them off
    if s == 1:
        hyper_rect = False
        exact_N = False

    # calculate the number of dimensions that need size n + 1
    n_plus1 = []
    if hyper_rect:
            x = 0; y = 0
            while True:
                y = math.ceil(n)**(x) * math.floor(n)**(s-x)
                if y >= N: break
                x += 1
            '''
            if x > 0:
                yl = math.ceil(n)**(x-1) * math.floor(n)**(s-(x-1))
                if N - yl < y - N:
                    x -= 1
            '''

            # need x of the dimensions to be size n+1,
            # the rest will be n.  choose randomly
            # which dimensions are n+1.
            arr = [i for i in range(s)]
            random.shuffle(arr)
            n_plus1 = arr[0:x]

    # Xs will contain the partitions, per dimension
    Xs = [i for i in range(s)]

    # Ts is a template used to build Xs[i]
    Ts = [i for i in range(int(n)+1)]

    for i in range(s):
        if hyper_rect:
            Xs[i] = Ts[:] if i in n_plus1 else Ts[:-1]
        elif s == 1:
            Xs[i] = Ts[:-1]
        else:
            # this is the hypercube, size n+1 in all dim
            Xs[i] = Ts[:]

    # call the sX() function
    fn = '_s' + str(s)
    bfs = globals()[fn](Xs)

    if shuffle:
        random.shuffle(bfs)
        if exact_N:
            if N <= len(bfs):
                bfs = bfs[:N]
            '''
            else:
                rs = rand.rand_seq(s=s, N=N-len(bfs))
                bfs += rs
            '''

    return bfs

#test
#nums = bfs_seq(s=7, N=10000, hyper_rect=True, shuffle=True, exact_N=True)
#print(len(nums))
#print(nums[:10])

