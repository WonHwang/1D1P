# 1D1P Day141 BOJ 11054번 가장 긴 바이토닉 부분 수열 문제 - 2021.03.25

N = int(input())
numbers = list(map(int, input().split()))
DP1 = [0] * N
DP2 = [0] * N

DP1[0], DP2[0] = 1, 1

for i in range(1, N):
    for j in range(i+1):
        if numbers[i] > numbers[j] and DP1[j] > DP1[i]:
            DP1[i] = DP1[j]
    DP1[i] += 1

numbers = numbers[::-1]
for i in range(1, N):
    for j in range(i+1):
        if numbers[i] > numbers[j] and DP2[j] > DP2[i]:
            DP2[i] = DP2[j]
    DP2[i] += 1
DP2 = DP2[::-1]

Max = 0
for i in range(N):
    if DP1[i] + DP2[i] > Max:
        Max = DP1[i] + DP2[i]

print(Max - 1)