# 1D1P Day78 SWEA 2001번 파리 퇴치 문제 - 2021.01.21

T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    area = []
    for i in range(N):
        area.append(list(map(int, input().split(' '))))
    
    maximum = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            tmp = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    tmp += area[x][y]
            if tmp > maximum:
                maximum = tmp
    
    print(f"#{_+1} {maximum}")