# 1D1P Day157 BOJ 2693번 N번째 큰 수 문제 - 2021.04.10

for tc in range(int(input())):
    A = list(map(int, input().split()))
    A.sort()
    print(A[-3])