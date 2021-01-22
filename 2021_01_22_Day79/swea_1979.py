# 1D1P Day79 SWEA 1979번 어디에 단어가 들어갈 수 있을까 문제 - 2021.01.22

for _ in range(1, int(input())+1):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(input().split())
    
    howmany = 0
    for i in range(N):
        num = 0
        for j in range(N):
            if puzzle[i][j] == '1':
                num += 1
            else:
                if num == K:
                    howmany += 1
                num = 0
        if num == K:
            howmany += 1
    
    for i in range(N):
        num = 0
        for j in range(N):
            if puzzle[j][i] == '1':
                num += 1
            else:
                if num == K:
                    howmany += 1
                num = 0
        if num == K:
            howmany += 1
    
    print(f"#{_} {howmany}")