# 1D1P Day96 BOJ 10972번 다음 순열 문제 - 2021.02.08

N = int(input())
target = list(map(int, input().split()))

i = len(target) - 1

answer = 1

if target == list(range(1,N+1))[::-1]:
    result = [-1]
    answer = 0

while answer:
    if target[i] - target[i-1] > 0:
        for j in range(len(target)-1, -1, -1):
            if target[i-1] < target[j]:
                target[i-1], target[j] = target[j], target[i-1]
                break
        result = target[:i] + sorted(target[i:])
        answer = 0
    i -= 1

for num in result:
    print(num, end=" ")
print()