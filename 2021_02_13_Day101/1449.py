# 1D1P Day101 BOJ 1449번 수리공 항승 문제 - 2021.02.13

N, L = map(int, input().split())
target = list(map(int, input().split()))
pipe = [1] * 1001

for point in target:
    pipe[point] = 0

answer = 0
for i in range(1001):
    if pipe[i] == 0:
        if i + L <= 1000:
            for j in range(L):
                pipe[i+j] = 1
            answer += 1
        else:
            for j in range(0, 1001-i):
                pipe[i+j] = 1
            answer += 1

print(answer)