# 1D1P Day367 BOJ 20499번 Darius님 한타 안 함? 문제 - 2021.11.06

K, D, A = map(int, input().split('/'))

if not D or K + A < D:
    print('hasu')
else:
    print('gosu')