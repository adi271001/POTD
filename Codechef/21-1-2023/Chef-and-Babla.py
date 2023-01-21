Question Link: https://www.codechef.com/problems/BAB_I
    
import heapq
import operator
import itertools
import sys
import functools
import bisect
import math
import random
import statistics
from collections import Counter
RTM1 = 1e9 + 7
RTM2 = 998244353
def fact(a):
    if a == 1 or a == 0:
        return 1
    return a * fact(a - 1)
def prod(c, d):
    if c == 0 or d == 0:
        return 0
    return c + prod(c, d - 1)
for _ in range (int(input())):
    a = int(input())
    h = [abs(int(y)) for y in input().split()]
    h.sort()
    if h[0] == 0:
        print(-1)
    else:
        print(h[0]-1)
