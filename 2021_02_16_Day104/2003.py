# 1D1P Day104 BOJ 2003번 수들의합2 문제 - 2021.02.16

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 0
total = numbers[0]
answer = 0

while start <= end:
    
    if end == N-1 and total <= M:
        if total == M:
            answer += 1
        break

    if total == M:
        end += 1
        total += numbers[end]
        answer += 1
    
    elif start == end and end < N-1:
        end += 1
        total += numbers[end]

    elif total > M or end == N-1:
        total -= numbers[start]
        start += 1
    
    elif total < M:
        end += 1
        total += numbers[end]

print(answer)