# 1D1P Day139 BOJ 11723번 집합 문제 - 2021.03.23

from sys import stdin
input = stdin.readline

M = int(input())

Set = [0] * 21
All = [1] * 21
empty = [0] * 21
answer = []

for _ in range(M):
    command = list(input().rstrip().split())
    if command[0] == "add":
        Set[int(command[1])] = 1
    
    elif command[0] == "remove":
        Set[int(command[1])] = 0
    
    elif command[0] == "check":
        print(Set[int(command[1])])
    
    elif command[0] == "toggle":
        if Set[int(command[1])]:
            Set[int(command[1])] = 0
        else:
            Set[int(command[1])] = 1
    
    elif command[0] == "all":
        Set = All[:]
    
    elif command[0] == "empty":
        Set = empty[:]