# 1D1P Day135 BOJ 5639번 이진 검색 트리 문제 - 2021.03.19

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

numbers = []

def postorder(start, end):

    if start > end:
        return
    
    idx = end + 1

    for i in range(start+1, end+1):
        if numbers[i] > numbers[start]:
            idx = i
            break
    
    postorder(start+1, idx-1)
    postorder(idx, end)

    print(numbers[start])

while True:
    try:
        numbers.append(int(input()))
    
    except:
        break

postorder(0, len(numbers)-1)

import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

numbers = []

def postorder(start, end):

    if start > end:
        return
    
    idx = start + 1

    while idx <= end:
        if numbers[idx] > numbers[start]:
            break
        idx += 1
    
    postorder(start+1, idx-1)
    postorder(idx, end)

    print(numbers[start])

while True:
    try:
        numbers.append(int(input()))
    
    except:
        break

postorder(0, len(numbers)-1)