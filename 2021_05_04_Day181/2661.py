# 1D1P Day181 BOJ 2661번 좋은수열 문제 - 2021.05.04

flag = False

def dfs(element, depth, N):

    global flag
    
    if depth > 1:
        if element[-1] == element[-2]:
            return

    for i in range(2, depth):
        for j in range(depth - i):
            if element[j:j+i] == element[j+i:j+2*i]:
                return
    
    if depth == N:
        print(''.join(element))
        flag = True
        return

    for i in range(1, 4):
        element.append(str(i))
        dfs(element, depth+1, N)
        if flag:
            return
        element.pop()

N = int(input())
dfs([], 0, N)