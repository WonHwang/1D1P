# 1D1P Day267 BOJ 2947번 나무 조각 문제 - 2021.07.29

nums = list(map(int, input().split()))

while nums != [1, 2, 3, 4, 5]:

    for i in range(4):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums)