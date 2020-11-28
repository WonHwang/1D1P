# 1D1P Day24 BOJ 2161번 카드1 문제 - 2020.11.28

from collections import deque

N = int(input())

queue = deque()

for i in range(1, N+1):
    queue.append(i)

answer = ""

while queue:
    answer += str(queue.popleft()) + " "
    if queue:
        tmp = queue.popleft()
        queue.append(tmp)

answer = answer[:-1]
print(answer)