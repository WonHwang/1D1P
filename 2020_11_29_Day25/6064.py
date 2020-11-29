# 1D1P Day25 BOJ 6064번 카잉달력 문제 - 2020.11.29 - pypy3로 제출해야 통과

import sys

T = int(input())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if M < N:
        visited = [0] * (N+1)
        start = [x, x]
        answer = x
        while start != [x, y]:
            a = start[0]
            b = start[1]

            b = (b + M) % N
            if b == 0:
                b = N
            
            if visited[b] == 1:
                answer = -1
                break

            visited[b] = 1
            
            answer += M
            start = [a, b]
    
    else:
        visited = [0] * (M+1)
        start = [y, y]
        answer = y
        while start != [x, y]:
            a = start[0]
            b = start[1]

            a = (a + N) % M
            if a == 0:
                a = M
            
            if visited[a] == 1:
                answer = -1
                break
            visited[a] = 1

            answer += N
            start = [a, b]
    
    print(answer)