from itertools import product
from math import prod
from numpy.random import choice


def probability(x, o):
    return len(x)/len(o)


def conditional_probability(x, y):
    return len(x & y)/len(y)


omega = set(product(['H', 'T'], repeat=20))

A = {om for om in omega if om.count('H') % 2 == 0}
B = {om for om in omega if om.count('T') < 4}
# print(conditional_probability(A, B))

omega = set(product([1,2,3,4,5,6], repeat=5))
A = {om for om in omega if sum(om) % 3 == 0}
B = {om for om in omega if prod(om) > 500}
# print(conditional_probability(B,A))

# Discrete random variable given by values and probabilities

# print(choice([1, 2, 4], p=[0.2, 0.5, 0.3]))

def count_frequencies(data, relative=False):
    counter = {}
    for element in data:
        if element not in counter:
            # get this element for the first time
            counter [element] = 1
        else:
            counter[element] += 1

    if relative:
        for element in counter:
            counter[element] /= len(data)

    return counter

sample =[choice([1, 2, 4], p=[0.2, 0.5, 0.3]) for _ in range(1000)]
# print(count_frequencies(sample))
# print(count_frequencies(sample, True))

# numpy array
sample = choice([1, 2, 4], p=[0.2, 0.5, 0.3], size=1000)
# print(sample)

import numpy as np
from scipy import stats as st
import itertools as it
import math

faculty_list = ['Physical','Economical','Mathematical','Psychological']

prob = {'Physical':1/6, 'Economical':1/4, 'Mathematical': 1/3, 'Psychological': 1/4}

def get_prob(var, prob):
    pr = 1
    n = len(var)
    for k, v in prob.items():
        m = var.count(k)
        pr *= v**m/(math.factorial(m))
    return pr*math.factorial(n)

pp = 0
for i in [x for x in list(it.combinations_with_replacement(faculty_list, 4)) if x.count('Mathematical') >= 2 or \
         (x.count('Mathematical') == 1 and x.count('Physical') == 1 and x.count('Economical') == 1 and x.count('Psychological') == 1)]:
    print(i, get_prob(i, prob))
    pp += get_prob(i, prob)
print('\nTotal: ', pp)




