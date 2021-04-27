# 1D1P Day174 BOJ 1647번 도시 분할 계획 문제 - 2021.04.27

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def isParent(idx):

    if idx != parent[idx]:
        parent[idx] = isParent(parent[idx])
    return parent[idx]

def Union(a, b):
    pa = isParent(a)
    pb = isParent(b)

    if pa < pb:
        parent[pa] = pb
    
    else:
        parent[pb] = pa

def isCycle(a, b):
    pa = isParent(a)
    pb = isParent(b)

    if pa == pb:
        return True
    
    return False

N, M = map(int, input().split())

roads = []
for _ in range(M):
    a, b, w = map(int, input().split())
    roads.append([w, a, b])

roads.sort()

parent = [i for i in range(N+1)]

answer = 0
Max = 0

for w, a, b in roads:
    if not isCycle(a, b):
        Union(a, b)
        answer += w
        if w > Max:
            Max = w

print(answer - Max)