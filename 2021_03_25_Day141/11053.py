# 1D1P Day141 BOJ 11053번 가장 긴 증가하는 부분 수열 문제 - 2021.03.25

N = int(input())
numbers = list(map(int, input().split()))
DP = [0] * N
DP[0] = 1


for i in range(1, N):
    for j in range(i+1):
        if numbers[i] > numbers[j] and DP[j] > DP[i]:
            DP[i] = DP[j]
    
    DP[i] += 1

print(max(DP))