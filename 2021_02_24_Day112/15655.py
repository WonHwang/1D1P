# 1D1P Day112 BOJ 15655번 N과 M (6) 문제 - 2021.02.24

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def printnumber(element):
    for i in range(M):
        print(numbers[element[i]], end = ' ')
    print()

def back(element, idx, num):

    if num == M:
        printnumber(element)
        return
    
    if idx == N:
        return
    
    element.append(idx)
    back(element, idx+1, num+1)

    element.pop()
    back(element, idx+1, num)

back([], 0, 0)