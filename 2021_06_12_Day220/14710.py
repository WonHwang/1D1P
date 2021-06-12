# 1D1P Day220 BOJ 14710번 고장난 시계 문제 - 2021.06.12

t1, t2 = map(int, input().split())

if (t1 * 12) % 360 == t2:
    print("O")
else:
    print("X")