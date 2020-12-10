# 1D1P Day36 BOJ 1697번 숨바꼭질 문제 - 2020.12.10

from collections import deque

N, K = map(int, input().split(' '))

visited = [0] * 100001

queue = deque()
queue.append(N)
visited[N] = 1
while queue:
    position = queue.popleft()
    time = visited[position]

    if position == K:
        break
    
    if 2*position <= 100000:
        if visited[2*position] == 0:
            queue.append(2*position)
            visited[2*position] = time+1
    
    if position + 1 <= 100000:
        if visited[position+1] == 0:
            queue.append(position+1)
            visited[position+1] = time+1
    
    if position - 1 >= 0:
        if visited[position-1] == 0:
            queue.append(position-1)
            visited[position-1] = time+1

print(visited[K] - 1)