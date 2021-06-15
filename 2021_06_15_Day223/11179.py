# 1D1P Day223 BOJ 11179번 2진수 뒤집기 문제 - 2021.06.15

N = int(input())
binary = '0b' + bin(N)[2:][::-1]
print(int(binary, 2))