# 1D1P Day209 BOJ 10995번 별 찍기 - 20 문제 - 2021.06.01

N = int(input())

for i in range(N):
    if i%2:
        print(' ', end='')
    for j in range(N):
        print('* ', end='')
    print()