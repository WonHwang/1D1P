# 1D1P Day176 BOJ 16398번 행성 연결 문제 - 2021.04.29

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isParent(idx):
    if idx != parent[idx]:
        parent[idx] = isParent(parent[idx])
    return parent[idx]

def Union(a, b):
    pa, pb = isParent(a), isParent(b)

    if pa < pb:
        parent[pa] = pb
    else:
        parent[pb] = pa

def isCycle(a, b):
    pa, pb = isParent(a), isParent(b)

    if pa == pb:
        return True
    return False

N = int(input())

adj_array = []
for _ in range(N):
    adj_array.append(list(map(int, input().split())))

edges = []
for i in range(N):
    for j in range(N):
        if i != j:
            edges.append([adj_array[i][j], i+1, j+1])

edges.sort()

parent = [i for i in range(N+1)]

answer = 0
for w, a, b in edges:
    if not isCycle(a, b):
        Union(a, b)
        answer += w

print(answer)