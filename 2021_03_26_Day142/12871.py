# 1D1P Day142 BOJ 12871번 무한 문자열 문제 - 2021.03.26

def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b > 0:
        a, b = b, a%b
    
    return a


a = input()
b = input()
gcd_ = gcd(len(a), len(b))
a, b = a * (len(b) * gcd_), b * (len(a) * gcd_)

print(1 if a == b else 0)