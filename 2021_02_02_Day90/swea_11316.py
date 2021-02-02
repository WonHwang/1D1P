# 1D1P Day90 SWEA 11316번 주기 찾기 문제 - 2021.02.02

for t in range(1, int(input()) + 1):
    s, p, q, m = map(int, input().split())

    dp = [-1] * m

    dp[s] = 0
    i = 1
    gap = 0
    while True:
        tmp = ((p * s) + q) % m
        if i - dp[tmp] == gap:
            answer = gap
            break
        gap = i - dp[tmp]
        dp[tmp] = i
        i += 1
        s = tmp
    
    print(f"#{t} {answer}")