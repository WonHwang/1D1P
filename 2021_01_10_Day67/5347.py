# 1D1P Day67 BOJ 5347번 LCM 문제 - 2021.01.10

from sys import stdin

def gcd(a, b):
    if b > a:
        big, small = b, a
    else:
        big, small = a, b
    
    r = big % small
    while r != 0:
        big, small = small, r
        r = big % small
    
    return small

T = int(stdin.readline().rstrip())
for _ in range(T):
    a, b = map(int, stdin.readline().rstrip().split(' '))
    print(a * b // gcd(a,b))