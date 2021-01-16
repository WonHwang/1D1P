# 1D1P Day73 BOJ 10156번 과자 문제 - 2021.01.16

K, N, M = map(int, input().split(' '))
if N * K >= M:
    print(N*K - M)
else:
    print(0)