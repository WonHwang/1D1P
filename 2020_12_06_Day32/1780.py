# 1D1P Day32 BOJ 1780번 종이의 개수 문제 - 2020.12.06

from sys import stdin

N = int(stdin.readline().rstrip())

paper = []

for i in range(N):
    paper.append(stdin.readline().rstrip().split(' '))

cnt = {'0' : 0, '1' : 0, '-1' : 0}

def check(N, x, y):
    target = paper[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if paper[i][j] != target:
                return False
    
    return True

def daq(N, x, y):
    if check(N, x, y):
        target = paper[x][y]
        cnt[target] += 1
    
    else:
        M = N // 3
        daq(M, x, y)
        daq(M, x+M, y)
        daq(M, x+(2*M), y)
        daq(M, x, y+M)
        daq(M, x+M, y+M)
        daq(M, x+(2*M), y+M)
        daq(M, x, y+(2*M))
        daq(M, x+M, y+(2*M))
        daq(M, x+(2*M), y+(2*M))


daq(N, 0, 0)
print(cnt['-1'])
print(cnt['0'])
print(cnt['1'])