# 1D1P Day197 BOJ 2702번 초6 수학 문제 - 2021.05.20

def gcd(a, b):

    if b > a:
        a, b = b, a

    while b != 0:
        a, b = b, a%b
    
    return a

for tc in range(int(input())):

    a, b = map(int, input().split())
    gcd_ = gcd(a, b)

    print(a*b//gcd_, gcd_)