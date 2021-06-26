# 1D1P Day234 BOJ 14915번 진수 변환기 문제 - 2021.06.26

notation = '0123456789ABCDEF'

def dectobase(number, base):

    q, r = number // base, number % base
    n = notation[r]

    return dectobase(q, base) + n if q else n

m, n = map(int, input().split())
print(dectobase(m, n))