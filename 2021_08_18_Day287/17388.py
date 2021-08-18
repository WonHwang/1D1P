# 1D1P Day287 BOJ 17388번 와글와글 숭고한 문제 - 2021.08.18

nums = list(map(int, input().split()))

if sum(nums) >= 100:
    print('OK')

else:
    print(['Soongsil', 'Korea', 'Hanyang'][nums.index(min(nums))])