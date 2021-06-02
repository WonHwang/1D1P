# 1D1P Day210 BOJ 10807번 개수 세기 문제 - 2021.06.02

N = int(input())
nums = list(map(int, input().split()))
count = dict()
for num in nums:
    count[num] = count.get(num, 0) + 1

print(count.get(int(input()), 0))