# 1D1P Day39 BOJ 5430번 AC 문제 - 2020.12.13

from sys import stdin
from collections import deque

T = int(input())

for _ in range(T):
    order = stdin.readline().rstrip()
    order_length = len(order)
    reverse = False

    arr_length = int(stdin.readline().rstrip())

    arr = stdin.readline().rstrip()
    arr = arr[1:-1].split(',')
    queue = deque()
    
    for i in range(arr_length):
        queue.append(int(arr[i]))
    
    error = 0
    for i in range(order_length):
        try:
            if order[i] == 'R':
                reverse = not reverse
            elif order[i] == 'D':
                if reverse:
                    queue.pop()
                else:
                    queue.popleft()
        except:
            error = 1
            break
    
    if error:
        print("error")
    else:
        answer = ""
        if reverse:
            while queue:
                answer += str(queue.pop())
                answer += ','
        else:
            while queue:
                answer += str(queue.popleft())
                answer += ','
        answer = "[" + answer[:-1] + "]"
        print(answer)