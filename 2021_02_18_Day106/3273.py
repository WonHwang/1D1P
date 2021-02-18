# 1D1P Day106 BOJ 3273번 두수의 합 문제 - 2021.02.18

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
target = int(input())
numbers.sort()

start = 0
end = N-1
answer = 0

while start < end:

    tmp = numbers[start] + numbers[end]

    if tmp == target:
        answer += 1
        start += 1
        end -= 1
    
    elif tmp > target:
        end -= 1
    
    else:
        start += 1

print(answer)