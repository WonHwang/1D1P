# 1D1P Day285 BOJ 6131번 완전 제곱수 문제 - 2021.08.16

square = [0] * 251001

for i in range(1, 501):
    square[i**2] = 1

N = int(input())
answer = 0

for i in range(1, 501):
    if square[i**2] and square[(i**2) + N]:
        answer += 1

print(answer)