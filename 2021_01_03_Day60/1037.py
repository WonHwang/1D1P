# 1D1P Day60 BOJ 1037번 약수 문제 - 2021.01.03

N = int(input())
factors = list(map(int, input().split(' ')))

factors.sort()
print(factors[0] * factors[-1])