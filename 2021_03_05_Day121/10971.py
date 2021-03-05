# 1D1P Day121 BOJ 10971번 외판원 순회 2 문제 - 2021.03.05

from sys import stdin
input = stdin.readline

N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().rstrip().split())))

answer = 10000000
visited = [0] * N
def dfs(now, cost, depth, start):

    global answer
    
    if cost > answer:
        return
    
    if depth == N-1:
        if maps[now][start] != 0:
            tmp = cost + maps[now][start]
            if tmp < answer:
                answer = tmp
        return
    
    for i in range(N):
        if visited[i] == 0 and maps[now][i] != 0:
            visited[i] = 1
            dfs(i, cost + maps[now][i], depth+1, start)
            visited[i] = 0

for i in range(N):
    visited[i] = 1
    dfs(i, 0, 0, i)
    visited[i] = 0

print(answer)