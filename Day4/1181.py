# 1D1P Day4 BOJ 1181번 단어 정렬 문제 - 2020.11.08

import sys

N = int(input())
array = ['0'] * N

for i in range(N):
    array[i] = sys.stdin.readline().rstrip()

array = list(set(array))

array.sort()

for i in range(51):
    for word in array:
        if len(word) == i:
            print(word)