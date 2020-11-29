# 1D1P Day25 BOJ 1021번 회전하는 큐 문제 - 2020.11.29

from collections import deque

N, M = map(int, input().split(' '))

queue = deque()
for i in range(1, N+1):
    queue.append(i)

position = input().split(' ')
for i in range(M):
    position[i] = int(position[i])

answer = 0

for i in range(M):
    length = len(queue)
    mid = int(length/2)
    tmp = queue.index(position[i])

    if tmp == 0:
        queue.popleft()
        continue

    elif tmp <= mid and tmp > 0:
        for k in range(tmp):
            queue.append(queue.popleft())
            answer += 1
    
    else:
        for k in range(length - tmp):
            queue.appendleft(queue.pop())
            answer += 1
    
    queue.popleft()

print(answer)