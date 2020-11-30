# 1D1P Day26 BOJ 11401번 이항 계수 3 문제 - 2020.11.30

N, K = map(int, input().split(' '))

mod = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % mod
    
    return result

def base2str(n):
    result = ""
    while n != 0:
        result = str(n%2) + result
        n = int(n/2)
    return result

def power(base, p):
    if p[0] == '0':
        result = 1
    else:
        result = base
    i = 1
    length = len(p)
    while i < length:
        base = (base ** 2) % mod
        if p[i] == '1':
            result = (result * base) % mod
        i += 1
    
    return result

pminus2 = base2str(mod-2)
pminus2_inverse = pminus2[::-1]
base = (factorial(K) * factorial(N-K)) % mod
inverse = power(base, pminus2_inverse)

result = (factorial(N) * inverse) % mod
print(result)