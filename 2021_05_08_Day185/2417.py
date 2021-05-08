# 1D1P Day185 BOJ 2417번 정수 제곱근 문제 - 2021.05.08

N = int(input())
answer = int(N**0.5)

print(answer if answer ** 2 == N else answer + 1)