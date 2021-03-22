# 1D1P Day138 SWEA 5650번 핀볼 게임 문제 - 2021.03.22

blackhole = []
wormhole = [[] for _ in range(5)]
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def init():
    global answer, blackhole, wormhole

    answer = 0
    blackhole = []
    wormhole = [[] for _ in range(5)]

def findhole(field, N):

    global wormhole, blackhole

    for i in range(N):
        for j in range(N):

            if 6 <= field[i][j] <= 10:
                wormhole[field[i][j] - 6].append([i, j])
            
            elif field[i][j] == -1:
                blackhole.append([i, j])

def move(start, direction, field, N):

    global answer, wormhole, blackhole

    x, y = start[0] + dx[direction], start[1] + dy[direction]

    score = 0
    while True:
        if [x, y] in blackhole or [x, y] == start:
            if score > answer:
                answer = score
            return
        
        if x < 0:
            score += 1
            x += 1
            direction = 0
        
        elif x == N:
            score += 1
            x -= 1
            direction = 1
        
        elif y < 0:
            score += 1
            y += 1
            direction = 2
        
        elif y == N:
            score += 1
            y -= 1
            direction = 3

        
        elif field[x][y] == 1:
            score += 1
            if direction == 0:
                direction = 2
                y += 1
            
            elif direction == 1:
                direction = 0
                x += 1
            
            elif direction == 2:
                direction = 3
                y -= 1
            
            elif direction == 3:
                direction = 1
                x -= 1
        
        elif field[x][y] == 2:
            score += 1
            if direction == 0:
                direction = 1
                x -= 1
            
            elif direction == 1:
                direction = 2
                y += 1
            
            elif direction == 2:
                direction = 3
                y -= 1
            
            elif direction == 3:
                direction = 0
                x += 1
        
        elif field[x][y] == 3:
            score += 1
            if direction == 0:
                direction = 1
                x -= 1
            
            elif direction == 1:
                direction = 3
                y -= 1
            
            elif direction == 2:
                direction = 0
                x += 1
            
            elif direction == 3:
                direction = 2
                y += 1
        
        elif field[x][y] == 4:
            score += 1
            if direction == 0:
                direction = 3
                y -= 1
            
            elif direction == 1:
                direction = 0
                x += 1
            
            elif direction == 2:
                direction = 1
                x -= 1
            
            elif direction == 3:
                direction = 2
                y += 1
        
        elif field[x][y] == 5:
            score += 1
            if direction == 0:
                direction = 1
                x -= 1
            
            elif direction == 1:
                direction = 0
                x += 1
            
            elif direction == 2:
                direction = 3
                y -= 1
            
            elif direction == 3:
                direction = 2
                y += 1
            
        elif 6 <= field[x][y] <= 10:
            tmp = field[x][y]
            tmp = wormhole[tmp - 6]

            if [x, y] == tmp[0]:
                x, y = tmp[1][0], tmp[1][1]
            else:
                x, y = tmp[0][0], tmp[0][1]
            
            if direction == 0:
                x += 1
            
            elif direction == 1:
                x -= 1
            
            elif direction == 2:
                y += 1
            
            elif direction == 3:
                y -= 1
        
        else:
            x += dx[direction]
            y += dy[direction]

for tc in range(1, int(input())+1):
    N = int(input())
    field = []
    init()
    for _ in range(N):
        field.append(list(map(int, input().split())))
    
    findhole(field, N)
    
    for i in range(N):
        for j in range(N):
            if field[i][j] == 0:
                for direction in range(4):
                    move([i, j], direction, field, N)
    
    print(f"#{tc} {answer}")