# 1D1P Day111 BOJ 13305번 주유소 문제 - 2021.02.23

import sys
input = sys.stdin.readline

N = int(input())
distance = list(map(int, input().rstrip().split()))
price = list(map(int, input().rstrip().split()))
price[N-1] = 0
distance.append(0)

answer = 0
min_price = price[0]
dist = distance[0]
for i in range(1, N):
    if min_price >= price[i]:
        answer += dist * min_price
        min_price = price[i]
        dist = 0
    dist += distance[i]

print(answer)