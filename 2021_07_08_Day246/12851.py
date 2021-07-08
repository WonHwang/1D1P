# 1D1P Day246 BOJ 12851번 숨바꼭질2 문제 - 2021.07.08

from collections import deque

N, K = map(int, input().split())
visited = [-1] * 100001
queue = deque()
queue.append(N)
visited[N] = 0
answer = 0

while queue:
    num = queue.popleft()
    if num == K:
        answer += 1
    
    for y in [num+1, num-1, num*2]:
        if 0 <= y < 100001:
            if visited[y] == -1 or visited[y] == visited[num] + 1:
                visited[y] = visited[num] + 1
                queue.append(y)

print(visited[K])
print(answer)