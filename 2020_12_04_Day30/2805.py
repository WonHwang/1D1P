# 1D1P Day30 BOJ 2805번 나무 자르기 문제 - 2020.12.04

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split(' '))

input_ = stdin.readline().rstrip().split(' ')

trees = [0] * N

for i in range(N):
    trees[i] = int(input_[i])

def check(height):
    result = 0
    for i in range(N):
        if trees[i] > height:
            result += trees[i] - height
    
    return result

front = 1
end = 1000000000

while front <= end:
    mid = int((front + end) / 2)

    get = check(mid)

    if get < M:
        end = mid - 1
    
    else:
        front = mid + 1

if check(mid) >= M:
    result = mid

else:
    result = mid - 1

print(result)