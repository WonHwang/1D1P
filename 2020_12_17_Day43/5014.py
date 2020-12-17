# 1D1P Day43 BOJ 5014번 스타트링크 문제 - 2020.12.17

from sys import stdin
from collections import deque

F, S, G, U, D = map(int, stdin.readline().rstrip().split(' '))

visited = [0] * (F+1)

queue = deque()
queue.append([S, 0])
visited[S] = 1
answer = -1
while queue:
    node = queue.popleft()
    now = node[0]
    step = node[1]
    if now == G:
        answer = step
        break
    if now + U <= F:
        if visited[now + U] == 0:
            queue.append([now + U, step + 1])
            visited[now + U] = 1
    if now - D >= 1:
        if visited[now - D] == 0:
            queue.append([now - D, step + 1])
            visited[now - D] = 1

if answer == -1:
    print("use the stairs")

else:
    print(answer)