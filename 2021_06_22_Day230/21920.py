# 1D1P Day230 BOJ 21920번 서로소 평균 문제 - 2021.06.22

def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b > 0:
        a, b = b, a%b
    
    return a

N = int(input())
A = list(map(int, input().split()))
X = int(input())

total = 0
cnt = 0
for num in A:
    if gcd(X, num) == 1:
        total += num
        cnt += 1

print(round(total / cnt, 6))