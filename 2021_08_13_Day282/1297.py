# 1D1P Day282 BOJ 1297번 TV 크기 문제 - 2021.08.13

D, H, W = map(int, input().split())

K = (D**2 / (H**2 + W**2))**0.5
h, w = int(H*K), int(W*K)

print(h, w)