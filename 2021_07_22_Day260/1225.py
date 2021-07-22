# 1D1P Day260 BOJ 1225번 이상한 곱셈 문제 - 2021.07.22

A, B = map(str, input().split())

target = [0] * 10

for i in range(10):
    tmp = 0
    for digit in B:
        tmp += int(digit) * i
    target[i] = tmp

answer = 0

for digit in A:
    answer += target[int(digit)]

print(answer)