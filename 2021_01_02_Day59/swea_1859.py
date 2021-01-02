# 1D1P Day59 SWEA 1859번 백만 장자 프로젝트 문제 - 2021.01.02

T = int(input())

for _ in range(T):

    N = int(input())

    seq = input().split(' ')[::-1]

    for i in range(N):
        seq[i] = int(seq[i])
    
    money = 0

    maximum = seq[0]
    total = 0
    number = 0

    for i in range(N):
        if seq[i] <= maximum:
            money += (maximum - seq[i])
        else:
            maximum = seq[i]

    print("#" + str(_ + 1) + " " + str(money))