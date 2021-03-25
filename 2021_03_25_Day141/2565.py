# 1D1P Day141 BOJ 2565번 전깃줄 문제 - 2021.03.25

from sys import stdin
input = stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().rstrip().split())))

numbers.sort(key=lambda x:x[0])

DP = [0] * N
DP[0] = 1

for i in range(1, N):
    for j in range(i+1):
        if numbers[i][1] > numbers[j][1] and DP[j] > DP[i]:
            DP[i] = DP[j]
    DP[i] += 1

print(N - max(DP))