# 1D1P Day50 BOJ 2630번 색종이 만들기 문제 - 2020.12.24

from sys import stdin

N = int(stdin.readline().rstrip())

paper = []

for _ in range(N):
    paper.append(stdin.readline().rstrip().split(' '))

def check(x, y, size):
    tmp = paper[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if paper[i][j] != tmp:
                return False
    return True

paper_blue = 0
paper_white = 0

def daq(x, y, size):
    global paper_blue, paper_white

    if check(x, y, size):
        if paper[x][y] == '1':
            paper_blue += 1
        else:
            paper_white += 1
    
    else:
        daq(x, y, size // 2)
        daq(x + size // 2, y, size // 2)
        daq(x, y + size // 2, size // 2)
        daq(x + size // 2, y + size // 2, size // 2)

daq(0, 0, N)
print(paper_white)
print(paper_blue)