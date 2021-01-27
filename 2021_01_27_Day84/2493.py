# 1D1P Day84 BOJ 2493번 탑 문제 - 2021.01.27

N = int(input())
numbers = list(map(int, input().split()))
result = [0] * N
stack = []
stack.append([numbers[N-1], N-1])
for i in range(N-2, -1, -1):
    while stack[-1][0] <= numbers[i]:
        node = stack.pop()
        result[node[1]] = i + 1
        if not stack:
            break
    stack.append([numbers[i], i])
for i in range(N):
    print(result[i], end = " ")