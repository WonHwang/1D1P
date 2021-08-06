# 1D1P Day275 BOJ 11966번 2의 제곱인가? 문제 - 2021.08.06

N = int(input())

answer = 1

while N > 1:

    if N % 2:
        answer = 0
        break
    N //= 2

print(answer)