# 1D1P Day107 JUNGOL 1523번 별삼각형1 문제 - 2021.02.19

n, m = map(int, input().split())

if n > 100 or not (m >= 1 and m <= 3):
    print('INPUT ERROR!')

elif m == 1:

    for i in range(n):
        for j in range(i+1):
            print('*', end = '')
        print()

elif m == 2:

    for i in range(n, 0, -1):
        for j in range(i):
            print('*', end = '')
        print()

elif m == 3:

    for i in range(1, n+1):
        for j in range(n-i):
            print(' ', end = '')
        for j in range(2*i-1):
            print('*', end = '')
        print()