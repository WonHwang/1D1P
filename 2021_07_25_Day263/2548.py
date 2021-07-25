# 1D1P Day263 BOJ 2548번 대표 자연수 문제 - 2021.07.25

N = int(input())
nums = list(map(int, input().split()))
answer, total = -1, 100000000

for i in range(1, 10001):
    tmp = 0
    for num in nums:
        tmp += abs(num - i)
        if tmp > total:
            break
    
    if tmp < total:
        total = tmp
        answer = i

print(answer)