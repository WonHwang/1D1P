# 1D1P Day83 BOJ 17608번 막대기 문제 - 2021.01.26

from sys import stdin

N = int(stdin.readline().rstrip())
stack = []
stack.append(int(stdin.readline().rstrip()))
for _ in range(N-1):
    number = int(stdin.readline().rstrip())
    while stack[-1] <= number:
        stack.pop()
        if not stack:
            stack.append(number)
            break
    else:
        stack.append(number)
print(len(stack))