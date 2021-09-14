# 1D1P Day314 BOJ 11170번 0의 개수 문제 - 2021.09.14

arr = [0] * 1000001

for i in range(1000001):
    tmp = str(i)
    for digit in tmp:
        if digit == '0':
            arr[i] += 1

for _ in range(int(input())):

    N, M = map(int, input().split())

    answer = 0
    for i in range(N, M+1):
        answer += arr[i]
    
    print(answer)