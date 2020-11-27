# 1D1P Day23 BOJ 18258번 큐 2 문제 - 2020.11.27

import sys

N = int(input())

front = 0
back = -1
queue = []

for i in range(N):
    command = sys.stdin.readline().rstrip().split(' ')
    
    if command[0] == 'push':
        queue.append(command[1])
        back += 1
    
    elif command[0] == 'pop':
        if front <= back:
            print(queue[front])
            front += 1
        else:
            print(-1)
    
    elif command[0] == 'front':
        if front <= back:
            print(queue[front])
        else:
            print(-1)
    
    elif command[0] == 'back':
        if front <= back:
            print(queue[back])
        else:
            print(-1)
    
    elif command[0] == 'size':
        print(back - front + 1)
    
    elif command[0] == 'empty':
        if front > back:
            print(1)
        else:
            print(0)