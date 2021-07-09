# 1D1P Day247 BOJ 13549번 숨바꼭질 3 문제 - 2021.07.09

from collections import deque

N, K = map(int, input().split())

queue = deque()
visited = [0] * 100001

queue.append(N)
visited[N] = 1

while queue:
    num = queue.popleft()
    step = visited[num]

    if 2*num < 100001 and not visited[2*num]:
        visited[2*num] = step
        queue.appendleft(2*num)

    if num == K:
        break

    for next in [num+1, num-1]:

        if 0 <= next < 100001 and not visited[next]:
            visited[next] = step + 1
            queue.append(next)

print(step-1)