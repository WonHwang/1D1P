# 1D1P Day78 BOJ 1026번 보물 문제 - 2021.01.21

N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort(reverse = True)

answer = 0
for i in range(N):
    answer += A[i] * B[i]

print(answer)