# 1D1P Day328 BOJ 20492번 세금 문제 - 2021.09.28

def tax(N):

    return int(N * 0.78)

N = int(input())
print(tax(N), int(N * 0.8 + tax(N * 0.2)))