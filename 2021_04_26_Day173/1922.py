# 1D1P Day173 BOJ 1922번 네트워크 연결 문제 - 2021.04.26

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

N = int(input())
M = int(input())
connections = []

for _ in range(M):
    a, b, w = map(int, input().split())
    connections.append([w, a, b])

parent = [i for i in range(N+1)]

connections.sort()

answer = 0
for w, a, b in connections:
    if not isCycle(a, b):
        Union(a, b)
        answer += w

print(answer)