# 1D1P Day342 BOJ 14491번 9진수 문제 - 2021.10.12

T = int(input())
answer = ''

while T:
    answer += str(T % 9)
    T //= 9

print(answer[::-1])