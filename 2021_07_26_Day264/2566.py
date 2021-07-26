# 1D1P Day264 BOJ 2566번 최대값 문제 - 2021.07.26

nums = []
for _ in range(9):
    nums.append(list(map(int, input().split())))

MAX = 0
x, y = -1, -1

for i in range(9):
    for j in range(9):
        if nums[i][j] >= MAX:
            MAX = nums[i][j]
            x, y = i, j

print(MAX)
print(x+1, y+1)