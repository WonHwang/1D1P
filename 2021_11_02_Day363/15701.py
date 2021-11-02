# 1D1P Day363 BOJ 15701번 순서쌍 문제 - 2021.11.02

N = int(input())

target = []

for i in range(1, int(N**0.5)+1):
    if not N%i:
        target.append(i)

answer = len(target)*2

if target[-1] ** 2 == N:
    answer -= 1

print(answer)