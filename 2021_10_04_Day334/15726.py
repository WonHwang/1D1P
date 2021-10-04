# 1D1P Day334 BOJ 15726번 이칙연산 문제 - 2021.10.04

a, b, c = map(int, input().split())

A = int((a * b) / c)
B = int((a / b) * c)
print(A if A > B else B)