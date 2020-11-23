# 1D1P Day19 BOJ 9466번 텀 프로젝트 문제 - 2020.11.23

import sys
from collections import deque

def main():
    N = int(input())
    input_ = sys.stdin.readline().rstrip().split(' ')
    students = [0] * (N+1)
    for i in range(1, N+1):
        students[i] = int(input_[i-1])
    
    result = [0] * (N+1)
    
    visited = [0] * (N+1)
    def cycle(start):
        queue = deque()
        tmp = start
        
        while visited[tmp] != 1:
            queue.append(tmp)
            visited[tmp] = 1
            tmp = students[tmp]
        if queue:
            front = queue.popleft()
            end = tmp

            while front != end:
                result[front] = -1
                if queue:
                    front = queue.popleft()
                else:
                    break
            if queue:
                result[front] = 1
                while queue:
                    result[queue.popleft()] = 1
    
    for i in range(1, N+1):
        if visited[i] == 0:
            cycle(i)
    
    answer = 0
    for i in range(1, N+1):
        if result[i] == -1:
            answer += 1
    
    print(answer)

T = int(input())
for i in range(T):
    main()