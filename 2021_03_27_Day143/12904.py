# 1D1P Day143 BOJ 12904번 A와 B 문제 - 2021.03.27

from collections import deque

answer = 0

def bfs(S, T):

    global answer

    queue = deque()
    queue.append(T)
    
    while queue:
        node = queue.popleft()
        if len(node) < len(S):
            break
        if node == S:
            answer = 1
            break

        if node[-1] == 'A':
            queue.append(node[:-1])
        else:
            queue.append(node[:-1][::-1])

S = input()
T = input()

bfs(S, T)
print(answer)