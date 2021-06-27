# 1D1P Day235 BOJ 1816번 암호 키 문제 - 2021.06.27

for tc in range(int(input())):
    N = int(input())
    for i in range(2, 1000001):
        if not N%i:
            print('NO')
            break
    else:
        print('YES')