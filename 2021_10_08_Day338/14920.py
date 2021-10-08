# 1D1P Day338 BOJ 14920번 3n+1 수열 문제 - 2021.10.08

C = int(input())
n = 1

while True:

    if C == 1:
        break

    if C%2:
        C *= 3
        C += 1
    
    else:
        C //= 2
    
    n += 1

print(n)