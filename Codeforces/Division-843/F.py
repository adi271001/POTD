Question Link: https://codeforces.com/contest/1775/problem/F
    
import re
import functools
import random
import sys
import os
import math
from collections import Counter, defaultdict, deque
from functools import lru_cache, reduce
from itertools import accumulate, combinations, permutations
from heapq import nsmallest, nlargest, heappushpop, heapify, heappop, heappush
from io import BytesIO, IOBase
from copy import deepcopy
import threading
from typing import *
from operator import add, xor, mul, ior, iand, itemgetter
import bisect
BUFSIZE = 4096
inf = float('inf')
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
sys.stdin = IOWrapper(sys.stdin)
sys.stdout = IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def I():
    return input()
 
def II():
    return int(input())
 
def MII():
    return map(int, input().split())
 
def LI():
    return list(input().split())
 
def LII():
    return list(map(int, input().split()))
 
def GMI():
    return map(lambda x: int(x) - 1, input().split())
 
def LGMI():
    return list(map(lambda x: int(x) - 1, input().split()))
 
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc
 
t, u = MII()
if u == 1:
    for _ in range(t):
        n = II()
        m = int(n ** 0.5)
        while True:
            if m * m >= n:
                c1, c2 = m, m
                break
            if m * (m + 1) >= n:
                c1, c2 = m, m + 1
                break
            m += 1
        ans = [['#' for _ in range(c2)] for _ in range(c1)]
        for i in range(c1 * c2 - n):
            ans[0][i] = '.'
        print(c1, c2)
        for line in ans:
            print(''.join(line))
else:
    mod = II()
    tmp = 701
    dp = [[0] * tmp for _ in range(tmp)]
    dp[0][0] = 1
    for i in range(tmp):
        for j in range(tmp):
            dp[i][j] = (dp[i][j-1] + dp[i-j][j]) % mod
    res = [dp[i][i] for i in range(tmp)]
    use2 = []
    for i in range(tmp):
        v = 0
        for j in range(i+1):
            v += res[j] * res[i-j]
            v %= mod
        use2.append(v)
    use4 = []
    for i in range(tmp):
        v = 0
        for j in range(i+1):
            v += use2[j] * use2[i-j]
            v %= mod
        use4.append(v)
    for _ in range(t):
        n = II()
        m = int(n ** 0.5)
        while True:
            if m * m >= n:
                c1, c2 = m, m
                break
            if m * (m + 1) >= n:
                c1, c2 = m, m + 1
                break
            m += 1
        ans = 0
        t = c1 + c2
        tmp = c1
        while tmp * (t - tmp) >= n:
            tmp -= 1
        k = tmp
        while True:
            if k * (t - k) >= n:
                ans += use4[k * (t - k) - n]
            elif k >= c2: break
            k += 1
        print((c1 + c2) * 2, ans % mod)
