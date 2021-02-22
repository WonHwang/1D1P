# 1D1P Day110 BOJ 2725번 보이는 점의 개수 문제 - 2021.02.22

def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b >= 1:
        a, b = b, a%b
    
    return a

DP = [0] * 1001
DP[1] = 3


for tc in range(int(input())):
    
    N = int(input())

    if DP[N] == 0:
        for i in range(1, N+1):
            if DP[i] == 0:
                tmp = 0
                for j in range(1, i+1):
                    if gcd(i, j) == 1:
                        tmp += 1 
                DP[i] = DP[i-1] + 2*tmp
    
    print(DP[N])