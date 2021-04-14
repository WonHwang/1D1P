# 1D1P Day161 SWEA 1244번 최대 상금 문제 - 2021.04.14

answer = 0

def money(numbers):

    answer = 0
    digit = 1

    for i in range(len(numbers)-1, -1, -1):
        answer += digit * numbers[i]
        digit *= 10
    
    return answer

def dfs(depth, numbers):

    global answer

    if depth == T:
        result = money(numbers)
        if result > answer:
            answer = result
        return
    
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] <= numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                if numbers not in visited[depth+1]:
                    visited[depth+1].append(numbers[:])
                    dfs(depth+1, numbers)
                numbers[i], numbers[j] = numbers[j], numbers[i]

for tc in range(1, int(input()) + 1):

    numbers, T = map(str, input().split())
    numbers = list(numbers)
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
    T = int(T)

    answer = 0

    visited = [[] for _ in range(T+1)]

    dfs(0, numbers)

    if not answer:
        if T % 2:
            numbers[-1], numbers[-2] = numbers[-2], numbers[-1]
        answer = money(numbers)
    print(f"#{tc} {answer}")