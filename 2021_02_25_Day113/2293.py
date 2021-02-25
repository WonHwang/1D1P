# 1D1P Day113 BOJ 2293번 동전 1 문제 - 2021.02.25

N, K = map(int, input().split())
price = [0] * 10001
coins = []
for _ in range(N):
    coins.append(int(input()))

price[0] = 1

for coin in coins:
    for i in range(1, K+1):
        if i - coin >= 0:
            price[i] += price[i - coin]

print(price[K])