# 1D1P Day40 programmers DFS/BFS 1번 타겟 넘버 문제 - 2020.12.14

from copy import deepcopy

answer = 0

def dfs(result, numbers, minus, target, depth, target_depth):
    global answer

    if depth == target_depth:
        if result == target:
            answer += 1
            return
        else:
            return
    
    dfs(result + numbers[depth], numbers, minus, target, depth + 1, target_depth)
    dfs(result + minus[depth], numbers, minus, target, depth + 1, target_depth)

def solution(numbers, target):

    minus = deepcopy(numbers)
    for i in range(len(numbers)):
        minus[i] = 0 - minus[i]
    
    dfs(0, numbers, minus, target, 0, len(numbers))
    
    return answer

print(solution([1,1,1,1,1], 3))