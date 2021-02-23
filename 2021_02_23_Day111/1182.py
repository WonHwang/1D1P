# 1D1P Day111 BOJ 1182번 부분수열의 합 문제 - 2021.02.23

import sys
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
answer = 0

for i in range(1, 2 ** N):
    tmp = bin(i)[2:].zfill(N)

    arr = []
    for j in range(N):
        if tmp[j]== '1':
            arr.append(numbers[j])
    
    if sum(arr) == S:
        answer += 1

print(answer)