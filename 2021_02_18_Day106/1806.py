# 1D1P Day106 BOJ 1806번 부분합 문제 - 2021.02.18

import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

start, end = 0, 0
length = N+1
total = numbers[0]

while True:

    if start > end:
        break

    if total >= S:
        tmp = end - start + 1
        if tmp < length:
            length = tmp
        
        total -= numbers[start]
        start += 1
    
    elif total < S:
        end += 1
        if end == N:
            break
        total += numbers[end]

print(length if length != N+1 else 0)