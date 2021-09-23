# 1D1P Day323 BOJ 1526번 가장 큰 금민수 문제 - 2021.09.23

nums = set()

for i in range(64):
    for j in range(1, 7):
        tmp = bin(i)[2:].zfill(j).replace('0', '4').replace('1', '7')
        nums.add(int(tmp))

nums = list(nums)
nums.sort(reverse=True)
N = int(input())

for num in nums:
    if num <= N:
        print(num)
        break