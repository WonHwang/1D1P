# 1D1P Day160 BOJ 3090번 차이를 최소로 문제 - 2021.04.13

from sys import stdin
input = stdin.readline

def binarysearch(mid, numbers, N):

    left_limit = [0] * N
    left_limit[0] = numbers[0]

    right_limit = [0] * N
    right_limit[N-1] = numbers[N-1]

    for i in range(1, N):
        left_limit[i] = min(numbers[i], left_limit[i-1] + mid)
        right_limit[N-1-i] = min(numbers[N-1-i], right_limit[N-i] + mid)
    
    limit = [0] * N
    for i in range(N):
        limit[i] = min(left_limit[i], right_limit[i])

    return limit
    
N, T = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

start = 0
end = (10 ** 9)

while start < end:

    mid = (start + end) // 2

    limit = binarysearch(mid, numbers, N)

    gap = 0
    for i in range(N):
        if numbers[i] > limit[i]:
            gap += (numbers[i] - limit[i])
    
    if gap > T:
        start = mid + 1
        mid += 1
    else:
        end = mid

limit = binarysearch(mid, numbers, N)

print(*limit)