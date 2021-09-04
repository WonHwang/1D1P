# 1D1P Day304 BOJ 2711번 오타맨 고창영 문제 - 2021.09.04

for _ in range(int(input())):

    N, string = map(str, input().split())
    N = int(N)

    answer = string[:N-1] + string[N:]
    print(answer)