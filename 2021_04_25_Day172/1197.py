# 1D1P Day172 BOJ 1197번 최소 스패닝 트리 문제 - 2021.04.25

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isParent(idx):
    if idx != parent[idx]:
        parent[idx] = isParent(parent[idx])
    return parent[idx]

def unionParent(x, y):
    px = isParent(x)
    py = isParent(y)

    if px < py:
        parent[px] = py
    
    else:
        parent[py] = px

def isCycle(x, y):
    px = isParent(x)
    py = isParent(y)

    if px == py:
        return True
    
    else:
        return False

V, E = map(int, input().split())

graph = []
for _ in range(E):
    a, b, w = map(int, input().split())
    graph.append([w, a, b])

graph.sort()
parent = [i for i in range(V+1)]

answer = 0
for cost, x, y in graph:
    if not isCycle(x, y):
        unionParent(x, y)
        answer += cost

print(answer)