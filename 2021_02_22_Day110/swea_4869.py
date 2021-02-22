# 1D1P Day110 SWEA 4869번 종이붙이기 문제 - 2021.02.22

DP = [0] * 301
DP[1] = 1
DP[2] = 3
for tc in range(1, int(input()) + 1):

    N = int(input()) // 10

    for i in range(N+1):
        if DP[i] == 0:
            DP[i] = DP[i-1] + 2 * DP[i-2]
    
    print(f"#{tc} {DP[N]}")