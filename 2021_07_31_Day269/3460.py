# 1D1P Day269 3460번 이진수 문제 - 2021.07.31

for tc in range(int(input())):

    N = int(input())
    N = bin(N)
    answer = []
    for i in range(len(N)-1, 1, -1):
        if N[i] == '1':
            answer.append(len(N)-i-1)
    print(*answer)