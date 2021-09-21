# 1D1P Day321 BOJ 15688번 수 정렬하기 5 문제 - 2021.09.21

from sys import stdin
input = stdin.readline

N = int(input())
nums = {}

for _ in range(N):
    num = int(input())
    nums[num] = nums.get(num, 0) + 1

for i in range(-1000000, 1000001):
    if i in nums:
        for _ in range(nums[i]):
            print(i)