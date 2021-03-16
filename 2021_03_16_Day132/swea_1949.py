dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

visited = []

answer = 0

def findtop(maps, N):
    top_list = []

    top = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] > top:
                top = maps[i][j]
    
    for i in range(N):
        for j in range(N):
            if maps[i][j] == top:
                top_list.append([i, j])
    
    return top, top_list

def dfs(value, x, y, maps, depth, K, did):

    global answer

    if depth > answer:
        answer = depth
    
    for i in range(4):
        a, b = x + dx[i], y + dy[i]

        if 0 <= a < N and 0 <= b < N and visited[a][b] == 0:
            if maps[a][b] < value:
                visited[a][b] = 1
                dfs(maps[a][b], a, b, maps, depth+1, K, did)
                visited[a][b] = 0
            
            elif not did and maps[a][b] - K < value:
                did = 1
                visited[a][b] = 1
                dfs(value - 1, a, b, maps, depth+1, K, did)
                visited[a][b] = 0
                did = 0
    

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))
    
    answer = 0

    top, top_list = findtop(maps, N)

    for tops in top_list:
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[tops[0]][tops[1]] = 1
        dfs(top, tops[0], tops[1], maps, 1, K, 0)
    
    print(f"#{tc} {answer}")