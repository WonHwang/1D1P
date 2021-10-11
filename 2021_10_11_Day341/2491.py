# 1D1P Day341 BOJ 2491번 수열 문제 - 2021.10.11

N = int(input())
nums = list(map(int, input().split()))
DP = [1] * N
DP2= [1] * N

for i in range(1, N):
    if nums[i] >= nums[i-1]:
        DP[i] = DP[i-1] + 1
    
    if nums[i] <= nums[i-1]:
        DP2[i] = DP2[i-1] + 1

print(max(max(DP), max(DP2)))