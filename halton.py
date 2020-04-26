#!/usr/bin/env python
# coding: utf-8

# Write a computer code for the Halton sequence. The input should be the
# dimension s and n, and the output should be the nth Halton vector where
# the bases are the first s prime numbers.

# About Halton Sequence
#
# Reference https://en.wikipedia.org/wiki/Halton_sequence

# imports
import math
import random


# Write a computer code for the Halton sequence.  The input should be
# the dimension s and n, and the output should be the nth Halton vector where
# the bases are the first s prime numbers.

def get_primes(N=1000):
    ''' get up to the first 1000 primes '''

    primes = []

    if N <= 1000:
        lines = []
        with open('1000.txt', 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    primes += line.split()

    primes = [int(p) for p in primes[:N]]
    return primes

primes = get_primes()

def halton(index, base):
    ''' return the nth number of a halton sequence with base
        implementation taken from pseudocode at
        https://en.wikipedia.org/wiki/Halton_sequence
    '''

    num = 0
    f = 1.0

    while (index > 0):

        f = f / base
        num = num + f * (index % base)
        index = math.floor((index / base))

    return num

def halton_vector(s, index, shift=False):
    ''' input: the dimension s (num of bases) and idx (Halton index)
        output: nth Halton vector where the bases are the first s prime numbers
    '''
    return [halton(index=index, base=primes[i]) for i in range(s)]


def halton_seq(s, N, shift=True):
    ''' return a list of N halton vectors (tuples) of dimension s '''

    hs = []

    offset = [random.random() for i in range(s)]

    for i in range(1, N+1):
        hv = halton_vector(s, i)
        if shift:
            hv = [((hv[i] + offset[i]) % 1) for i in range(s)]
        hs.append(tuple(hv))

    return hs

#test
#hs = halton_seq(s=2, N=100, shift=False)
#print(hs[:10])

