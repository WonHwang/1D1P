# 1D1P Day256 BOJ 12852번 1로 만들기 2 문제 - 2021.07.18

from collections import deque

visited = [0] * 1000001

def bfs(N):

    queue = deque()
    queue.append([1, 0])
    visited[1] = 1

    while queue:
        node = queue.popleft()
        x, step = node[0], node[1]

        if x == N:
            print(step)
            break

        for y in [3*x, 2*x, x+1]:
            if y < 1000001 and not visited[y]:
                visited[y] = x
                queue.append([y, step+1])

N = int(input())
bfs(N)
answer = []
while N != 1:
    answer.append(N)
    N = visited[N]
answer.append(1)
print(*answer)