# 1D1P Day85 BOJ 9663번 N-Queen 문제 - 2021.01.28
# C로 푼거 재풀이, Pypy3으로 해결

N = int(input())

answer = 0

def dfs(y, col, cross1, cross2):
    global answer
    if y == N:
        answer += 1
        return
    
    for i in range(N):
        if i in col:
            continue
        if y - i in cross1:
            continue
        if y + i in cross2:
            continue
        
        col.add(i)
        cross1.add(y-i)
        cross2.add(y+i)
        dfs(y+1, col, cross1, cross2)
        col.remove(i)
        cross1.remove(y-i)
        cross2.remove(y+i)

col, cross1, cross2 = set(), set(), set()

dfs(0, col, cross1, cross2)
print(answer)