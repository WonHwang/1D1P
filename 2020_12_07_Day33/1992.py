# 1D1P Day33 BOJ 1992번 쿼드트리 문제 - 2020.12.07

from sys import stdin

N = int(stdin.readline().rstrip())

arr = []
result = ""

for _ in range(N):
    arr.append(stdin.readline().rstrip())

def check(N, x, y):
    target = arr[x][y]

    for i in range(x, x+N):
        for j in range(y, y+N):
            if arr[i][j] != target:
                return False
    
    return True

def daq(N, x, y):
    global result

    if check(N, x, y):
        result += arr[x][y]
    
    else:
        result += '('
        M = N // 2
        daq(M, x, y)
        daq(M, x, y+M)
        daq(M, x+M, y)
        daq(M, x+M, y+M)
        result += ')'
    
daq(N, 0, 0)
print(result)