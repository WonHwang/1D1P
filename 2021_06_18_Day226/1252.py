# 1D1P Day226 BOJ 1252번 이진수 덧셈 문제 - 2021.06.18

a, b = map(str, input().split())
a = '0b' + a
b = '0b' + b
a = int(a, 2)
b = int(b, 2)
answer = bin(a+b)[2:]
print(answer)