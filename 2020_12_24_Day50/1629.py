# 1D1P Day50 BOJ 1629번 곱셈 문제 - 2020.12.24

from sys import stdin

A, B, C = map(int, stdin.readline().rstrip().split(' '))

B = bin(B)[2:][::-1]

answer = 1

target = A % C
for i in range(len(B)):
    if B[i] == '1':
        answer = (answer * target) % C
    target = (target ** 2) % C

print(answer)