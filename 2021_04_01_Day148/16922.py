# 1D1P Day148 BOJ 16922번 로마 숫자 만들기 문제 - 2021.04.01

N = int(input())

result = [0] * 2001

for i in range(N+1):
    for j in range(N+1-i):
        for k in range(N+1-i-j):
            l = N - i - j - k
            result[i + 5*j + 10*k + 50*l] = 1

answer = 0
for i in range(2001):
    if result[i]:
        answer += 1

print(answer)