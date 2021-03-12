# 1D1P Day128 BOJ 1292번 쉽게 푸는 문제 문제 - 2021.03.12

DP = [0] * 1001
DP[1] = 1

def cal():
    n = 2
    i = 2
    while True:
        for j in range(n):
            DP[i] = DP[i-1] + n
            i += 1
            if i == 1001:
                return
        n += 1
cal()
A, B = map(int, input().split())
print(DP[B] - DP[A-1])