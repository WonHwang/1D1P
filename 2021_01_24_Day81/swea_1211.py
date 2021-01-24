from collections import deque

for _ in range(1, 11):
    t = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))
    
    steps = [0] * 100

    for i in range(100):
        if ladder[0][i] == 1:
            visited = [[0 for __ in range(100)] for ___ in range(100)]
            queue = deque()
            queue.append([0, i])
            visited[0][i] = 1

            while queue:
                node = queue.popleft()
                x, y = node[0], node[1]
                step = visited[x][y]
                if x == 99:
                    steps[i] = step
                    break

                if y > 0:
                    if ladder[x][y-1] == 1 and visited[x][y-1] == 0:
                        queue.append([x, y-1])
                        visited[x][y-1] = step + 1
                        continue
                if y < 99:
                    if ladder[x][y+1] == 1 and visited[x][y+1] == 0:
                        queue.append([x, y+1])
                        visited[x][y+1] = step + 1
                        continue
                if x < 99:
                    if ladder[x+1][y] == 1 and visited[x+1][y] == 0:
                        queue.append([x+1, y])
                        visited[x+1][y] = step + 1
    
    index = 0
    mini = 10000
    for i in range(100):
        if steps[i] < mini and steps[i] != 0:
            mini = steps[i]
            index = i
    print(f"#{t} {index}")