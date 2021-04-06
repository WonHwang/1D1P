from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())

paper = []

for _ in range(N):
    paper.append(list(map(int, input().rstrip().split())))

visited = [[0 for _ in range(M)] for _ in range(N)]
answer = []

def bfs(a, b):
    
    visited[a][b] = 1
    queue = deque()
    queue.append([a, b])

    cnt = 1

    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]

        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < N and 0 <= y < M and paper[x][y] == 1 and visited[x][y] == 0:
                visited[x][y] = 1
                cnt += 1
                queue.append([x, y])
    
    answer.append(cnt)


for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and paper[i][j] == 1:
            bfs(i, j)

if answer:
    print(len(answer))
    print(max(answer))
else:
    print(0)
    print(0)