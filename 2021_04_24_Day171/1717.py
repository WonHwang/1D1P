# 1D1P Day171 BOJ 1717번 집합의 표현 문제 - 2021.04.24

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def Make_Set(N):
    return [i for i in range(N+1)]

def Find_Set(idx):
    if Set[idx] == idx:
        return idx
    Set[idx] = Find_Set(Set[idx])
    return Set[idx]

def Union(a, b):
    Set[Find_Set(a)] = Find_Set(b)

N, M = map(int, input().split())

Set = Make_Set(N)

for _ in range(M):
    oper, a, b = map(int, input().split())
    if oper:
        a_root = Find_Set(a)
        b_root = Find_Set(b)
        print("YES" if a_root == b_root else "NO")
    
    else:
        Union(a, b)