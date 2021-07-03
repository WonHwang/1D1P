# 1D1P Day241 BOJ 15969번 행복 문제 - 2021.07.03

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[N-1] - nums[0])