# 1D1P Day175 BOJ 6497번 전력난 문제 - 2021.04.28

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

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

while True:
    N, M = map(int, input().split())
    
    if N == 0 and M == 0:
        break
    
    roads = []
    for _ in range(M):
        a, b, w = map(int, input().split())
        roads.append([w, a+1, b+1])

    roads.sort()
    parent = [i for i in range(N+1)]

    answer = 0
    total = 0
    for w, a, b in roads:
        total += w
        if not isCycle(a, b):
            Union(a, b)
            answer += w

    print(total - answer)