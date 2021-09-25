# 1D1P Day325 BOJ 2033번 반올림 문제 - 2021.09.25

N = int(input())

tmp = 10

while N > tmp:

    if N % tmp >= 5*(tmp//10):
        N += tmp
    
    N -= N % tmp

    tmp *= 10

print(N)