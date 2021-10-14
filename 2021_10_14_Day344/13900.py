# 1D1P Day344 BOJ 13900번 순서쌍의 곱의 합 - 2021.10.14

N = int(input())
nums = list(map(int, input().split()))

answer = sum(nums) ** 2
tmp = 0
for i in range(N):
    tmp += nums[i]**2

print((answer-tmp)//2)