# 1D1P Day71 SWEA 2819번 격자판의 숫자 이어 붙이기 - 2021.01.14


T = int(input())

for _ in range(T):

    answer = set()
    board = []
    for i in range(4):
        board.append(input().split(' '))
    def dfs(x, y, result, depth):
        if depth == 7:
            answer.add(result)
            return
    
        if x > 0:
            dfs(x-1, y, result + board[x-1][y], depth + 1)
        if x < 3:
            dfs(x+1, y, result + board[x+1][y], depth + 1)
        if y > 0:
            dfs(x, y-1, result + board[x][y-1], depth + 1)
        if y < 3:
            dfs(x, y+1, result + board[x][y+1], depth + 1)
    
    for i in range(4):
        for j in range(4):
            dfs(i, j, "", 0)
    print(f"#{_+1}", len(answer))