# 1D1P Day83 SWEA 1225번 암호생성기 문제 - 2021.01.26

from collections import deque

for _ in range(10):
    t = int(input())
    numbers = list(map(int, input().split()))
    queue = deque()
    for i in range(8):
        queue.append(numbers[i])
    n = 1
    while True:
        number = queue.popleft()
        number -= n
        if number <= 0:
            queue.append(0)
            break
        queue.append(number)
        n = (n % 5) + 1
    answer = ""
    while queue:
        answer += str(queue.popleft()) + " "
    print(f"#{t} {answer[:-1]}")
