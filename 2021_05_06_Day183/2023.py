# 1D1P Day183 BOJ 2023번 신기한 소수 문제 - 2021.05.06

N = int(input())

def isprime(N):

    if N == 2 or N == 3:
        return True
    
    for i in range(3, int(N ** 0.5)+1, 2):
        if not N % i:
            return False
    
    return True

def dfs(number, depth, N):

    if depth == N:
        print(number)
        return
    
    if depth == 0:
        for i in [2, 3, 5, 7]:
            number += i
            dfs(number, depth+1, N)
            number //= 10
    
    else:
        for i in [1, 3, 5, 7, 9]:
            number = (number * 10) + i
            if isprime(number):
                dfs(number, depth+1, N)
            
            number //= 10

dfs(0, 0, N)