# 1D1P Day61 BOJ 9375번 패션왕 신해빈 문제 - 2021.01.04

T = int(input())

for _ in range(T):
    N = int(input())

    clothes = dict()

    for __ in range(N):
        a, b = input().split(' ')

        if b not in clothes:
            clothes[b] = 1
        
        else:
            clothes[b] += 1
    
    result = 1

    for key in clothes:
        result *= clothes[key] + 1
    
    print(result - 1)