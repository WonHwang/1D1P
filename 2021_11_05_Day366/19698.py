# 1D1P Day366 BOJ 19698번 헛간 청약 문제 - 2021.11.05

N, W, H, L = map(int, input().split())

answer = (W//L) * (H//L)

print(answer if answer <= N else N)