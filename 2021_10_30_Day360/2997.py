# 1D1P Day360 BOJ 2997번 네 번째 수 문제 - 2021.10.30

nums = list(map(int, input().split()))

for i in range(-200, 201):
    nums.append(i)
    nums_ = sorted(nums)

    if 2*nums_[1] == nums_[0] + nums_[2] and 2*nums_[2] == nums_[1] + nums_[3]:
        print(i)
        break

    nums.pop()