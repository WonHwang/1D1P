# 1D1P Day23 BOJ 11866번 요세푸스 문제 0 - 2020.11.27

from collections import deque

N, K = map(int, input().split(' '))

queue = deque()

for i in range(1, N+1):
    queue.append(i)

answer = "<"
tmp = 1
while queue:
    if tmp == K:
        answer += str(queue.popleft()) + ", "
        tmp = 1
        continue
    queue.append(queue.popleft())
    tmp += 1

answer = answer[:-2] + ">"
print(answer)