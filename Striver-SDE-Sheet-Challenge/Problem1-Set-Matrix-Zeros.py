from math import *
from collections import *
from sys import *
from os import *
from typing import List
def setZeros(matrix: List[List[int]]) -> None:
    rwz = set()
    cwz = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rwz.add(i)
                cwz.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rwz or j in cwz:
                matrix[i][j] = 0
    return matrix
