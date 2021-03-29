from sys import stdin
input = stdin.readline

N, K = map(int, input().split())

answer = 1
for i in range(2, N+1):
    answer = ((answer + K-1) % i) + 1

print(answer)