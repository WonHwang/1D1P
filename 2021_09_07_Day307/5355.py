# 1D1P Day307 BOJ 5355번 화성 수학 문제 - 2021.09.07

from sys import stdin
input = stdin.readline

for _ in range(int(input())):

    line = list(input().split())
    answer = float(line.pop(0))

    for op in line:
        if op == '@':
            answer *= 3
        
        elif op == '%':
            answer += 5
        
        elif op == '#':
            answer -= 7
    
    print("%.2f"%(answer))