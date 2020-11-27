# 1D1P Day23 BOJ 2164번 카드2 문제 - 2020.11.27

from collections import deque

N = int(input())

queue = deque()

for i in range(1, N+1):
    queue.append(i)

while N > 1:
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
    N -= 1

print(queue.popleft())