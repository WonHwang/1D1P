# 1D1P Day64 BOJ 1735번 분수 합 문제 - 2021.01.07

def lcm(p, q):

    big = p
    small = q
    if q > p:
        big = q
        small = p
    
    lcm = big

    while lcm % small != 0:
        lcm += big
    
    return lcm

def gcd(p, q):

    big = p
    small = q
    if q > p:
        big = q
        small = p
    
    r = 1
    while r != 0:
        r = big % small
        big, small = small, r

    return big 

a, b = map(int, input().split(' '))
c, d = map(int, input().split(' '))

lcm_ = lcm(b, d)
result = a * int(lcm_ / b) + c * int(lcm_ / d)
gcd_ = gcd(result, lcm_)

print(int(result / gcd_), int(lcm_ / gcd_))