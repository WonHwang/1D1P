# 1D1P Day112 BOJ 14888번 연산자 끼워넣기 문제 - 2021.02.24

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
opers = list(map(int, input().split()))


Max = -1000000001
Min = 1000000001

visited = [0] * (N-1)

def divide(a, b):
    
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        a, b = abs(a), abs(b)
        q = a // b
        return -q
    
    return a // b

def cal(element):
    global Max, Min
    
    tmp = numbers[0]
    for i in range(N-1):
        if element[i] == 0:
            tmp += numbers[i+1]
        elif element[i] == 1:
            tmp -= numbers[i+1]
        elif element[i] == 2:
            tmp *= numbers[i+1]
        elif element[i] == 3:
            tmp = divide(tmp, numbers[i+1])
    if tmp > Max:
        Max = tmp
    if tmp < Min:
        Min = tmp


def permutation(element, depth):
    
    if depth == N-1:
        cal(element)
        return
    
    for i in range(4):
        if opers[i] != 0:
            element.append(i)
            opers[i] -= 1
            permutation(element, depth + 1)
            opers[i] += 1
            element.pop()

permutation([], 0)


print(Max)
print(Min)