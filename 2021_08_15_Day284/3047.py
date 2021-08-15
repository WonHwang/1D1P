# 1D1P Day284 BOJ 3047번 ABC 문제 - 2021.08.15

nums = list(map(int, input().split()))
order = input()
nums.sort()
A, B, C = map(int, nums)

for i in range(3):
    if order[i] == 'A':
        print(A, end='')
    elif order[i] == 'B':
        print(B, end='')
    else:
        print(C, end='')
    
    if i < 2:
        print(end=' ')
    else:
        print()