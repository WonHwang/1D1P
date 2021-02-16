# 1D1P Day104 SWEA 1954번 달팽이 숫자 문제 - 2021.02.16

for tc in range(1, int(input()) + 1):

    N = int(input())

    box = [[0 for _ in range(N)] for _ in range(N)]

    x, y = 0, 0
    direction = 1
    for i in range(1, N*N + 1):
        box[x][y] = i

        if direction == 1:
            if y + 1 < N and box[x][y+1] == 0:
                y += 1
            else:
                direction = 2
                x += 1
        
        elif direction == 2:
            if x + 1 < N and box[x+1][y] == 0:
                x += 1
            else:
                direction = 3
                y -= 1
        
        elif direction == 3:
            if y - 1 >= 0 and box[x][y-1] == 0:
                y -= 1
            else:
                direction = 4
                x -= 1
        
        elif direction == 4:
            if x - 1 >= 0 and box[x-1][y] == 0:
                x -= 1
            else:
                direction = 1
                y += 1
    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(box[i][j], end = " ")
        print()