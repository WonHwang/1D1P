# 1D1P Day124 BOJ 1309번 동물원 문제 - 2021.03.08

N = int(input())

dp1 = [1] * (N+1)
dp2 = [0] * (N+1)

for i in range(1, N+1):
    dp2[i] = (dp1[i-1] - dp2[i-1]) % 9901
    dp1[i] = (dp1[i-1] + 2*dp2[i]) % 9901

print(dp1[N])