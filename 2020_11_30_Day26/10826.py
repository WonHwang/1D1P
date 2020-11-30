# 1D1P Day26 BOJ 10826번 피보나치 수 4 문제 - 2020.11.29

def fib(n):
    x = 0
    y = 1
    for i in range(n):
        x, y = y, x+y
    return x
print(fib(int(input())))