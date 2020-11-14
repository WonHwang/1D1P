# 1D1P Day10 BOJ 1676번 팩토리얼 0의 개수 문제 - 2020.11.14

N = int(input())
factorial = 1
answer = 0
while N > 1:
    factorial *= N
    while factorial % 10 == 0:
        factorial = int(factorial/10)
        answer += 1
    factorial = factorial % 10000
    N -= 1
print(answer)