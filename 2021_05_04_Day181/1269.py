# 1D1P Day181 BOJ 1269번 대칭 차집합 문제 - 2021.05.04

A, B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(A-B) + len(B-A))