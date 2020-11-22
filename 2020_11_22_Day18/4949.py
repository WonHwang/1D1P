# 1D1P Day18 BOJ 4949번 균형잡힌 세상 문제 - 2020.11.22

import sys
from collections import deque

while True:
    string = sys.stdin.readline().rstrip()
    if string =='.':
        break
    stack = deque()
    top = 0
    length = len(string)
    result = 1
    for i in range(length):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
            top += 1
        elif string[i] == ')' or string[i] == ']':
            if top == 0:
                result = 0
                break
            tmp = stack.pop()
            top -= 1
            if tmp == '(' and string[i] == ']':
                result = 0
                break
            elif tmp == '[' and string[i] == ')':
                result = 0
                break
    if stack:
        result = 0
    
    if result == 1:
        print("yes")
    else:
        print("no")