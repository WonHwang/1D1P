# 1D1P Day70 BOJ 14490번 백대열 문제 - 2021.01.13

a, b = map(int, input().split(':'))
A = a
B = b
if B > A:
    A, B = B, A
r = A % B
while r != 0:
    B, r = r, B % r

print(str(a // B)  + ":" + str(b // B))