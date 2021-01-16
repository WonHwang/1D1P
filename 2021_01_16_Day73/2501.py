# 1D1P Day73 BOJ 2501번 약수 구하기 문제 - 2021.01.16

N, K = map(int, input().split(' '))
tmp = 0
for i in range(1, N+1):
    if N % i == 0:
        tmp += 1
        if tmp == K:
            break
if tmp == K:
    print(i)
else:
    print(0)