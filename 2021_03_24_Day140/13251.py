# 1D1P Day140 BOJ 13251번 조약돌 꺼내기 문제 - 2021.03.24

N = int(input())
stone = list(map(int, input().split()))
K = int(input())
total = sum(stone)
mother = 1
son = 0

for i in range(K):
    mother *= total-i

for i in range(N):
    if stone[i] >= K:
        tmp = 1
        for j in range(K):
            tmp *= stone[i] - j
        son += tmp
print("%0.16f"%(son / mother))