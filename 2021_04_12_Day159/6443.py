# 1D1P Day159 BOJ 6443번 애너그램 문제 - 2021.04.12

N = int(input())

def permutation(element, string, depth, visited):

    if depth == len(string):
        print(''.join(element))
        return
    
    disstep = '-1'
    for i in range(len(string)):
        if visited[i] == 0 and string[i] != disstep:
            visited[i] = 1
            element.append(string[i])
            disstep = string[i]
            permutation(element, string, depth+1, visited)
            element.pop()
            visited[i] = 0

for _ in range(N):
    string = list(input())
    string.sort()
    visited = [0] * len(string)
    permutation([], string, 0, visited)