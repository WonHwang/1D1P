# 1D1P Day207 BOJ 2592번 대표값 문제 - 2021.05.30

nums = [0] * 1001
total = 0
for _ in range(10):
    tmp = int(input())
    nums[tmp] += 1
    total += tmp

print(total // 10)
cnt = 0
for i in range(10, 1001, 10):
    if nums[i] > cnt:
        cnt = nums[i]

for i in range(10, 1001, 10):
    if nums[i] == cnt:
        print(i)
        break