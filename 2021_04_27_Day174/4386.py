# 1D1P Day174 BOJ 4386번 별자리 만들기 문제 - 2021.04.27

import sys
input = sys.stdin.readline

def distance(a, b):
    result = 0
    for i in range(2):
        result += (a[i] - b[i]) ** 2
    
    return result ** 0.5

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

stars = []

for _ in range(N):
    stars.append(list(map(float, input().split())))

stars = [[0, 0]] + stars
parent = [i for i in range(N+1)]

edges = []

for i in range(1, N+1):
    for j in range(1, N+1):
        if i != j:
            edges.append([distance(stars[i], stars[j]), i, j])

edges.sort()

answer = 0
for w, a, b in edges:
    if not isCycle(a, b):
        Union(a, b)
        answer += w

print("%.2f"%(answer))