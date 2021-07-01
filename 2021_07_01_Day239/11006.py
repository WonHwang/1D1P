# 1D1P Day239 BOJ 11006번 남욱이의 닭장 문제 - 2021.07.01

from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    N, M = map(int, input().split())
    result = 2*M - N
    print(result, M-result)