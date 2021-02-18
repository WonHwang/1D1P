# 1D1P Day106 BOJ 2470번 두 용액 문제 - 2021.02.18

import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().rstrip().split()))
liquid.sort()
Min = abs(liquid[0] + liquid[N-1])
answer1, answer2 = liquid[0], liquid[N-1]
start, end = 0, N-1

while start < end:

    tmp = liquid[start] + liquid[end]

    if tmp == 0:
        answer1, answer2 = liquid[start], liquid[end]
        break

    if tmp > 0:
        if abs(tmp) < Min:
            Min = abs(tmp)
            answer1, answer2 = liquid[start], liquid[end]
        end -= 1
    
    elif tmp < 0:
        if abs(tmp) < Min:
            Min = abs(tmp)
            answer1, answer2 = liquid[start], liquid[end]
        
        start += 1

print(answer1, answer2)