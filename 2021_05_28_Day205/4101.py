# 1D1P Day205 BOJ 4101번 크냐? 문제 - 2021.05.28

while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    print('Yes' if a > b else 'No')