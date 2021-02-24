# 1D1P Day112 BOJ 14889번 스타트와 링크 문제 - 2021.02.24

import sys
input = sys.stdin.readline

N = int(input())
S = []
answer = 1000000000

for _ in range(N):
    S.append(list(map(int, input().split())))

def eachscore(group):
    global answer

    other_group = []

    for i in range(N):
        if i not in group:
            other_group.append(i)

    score = 0
    for i in group:
        for j in group:
            score += S[i][j]

    other_score = 0
    for i in other_group:
        for j in other_group:
            other_score += S[i][j]

    tmp = abs(score - other_score)

    if tmp < answer:
        answer = tmp

def grouping(group, idx):

    if len(group) == N // 2:
        eachscore(group)
        return
    
    if idx == N:
        return
    
    group.append(idx)
    grouping(group, idx + 1)
    group.pop()
    grouping(group, idx + 1)


visited = [0] * (N)
grouping([], 0)

print(answer)