# 1D1P Day69 BOJ 1485번 정사각형 문제 - 2021.01.12

T = int(input())

for _ in range(T):
    x1, y1 = map(int, input().split(' '))
    x2, y2 = map(int, input().split(' '))
    x3, y3 = map(int, input().split(' '))
    x4, y4 = map(int, input().split(' '))

    arr = []

    arr.append((x1 - x2) ** 2 + (y1 - y2) ** 2)
    arr.append((x1 - x3) ** 2 + (y1 - y3) ** 2)
    arr.append((x1 - x4) ** 2 + (y1 - y4) ** 2)
    arr.append((x2 - x3) ** 2 + (y2 - y3) ** 2)
    arr.append((x2 - x4) ** 2 + (y2 - y4) ** 2)
    arr.append((x3 - x4) ** 2 + (y3 - y4) ** 2)

    edge = min(arr)
    cross = max(arr)

    num = 0
    for i in range(6):
        if arr[i] == edge:
            num += 1
    
    if num != 4:
        print(0)
        continue

    num = 0
    for i in range(6):
        if arr[i] == cross:
            num += 1
    
    if num != 2:
        print(0)
        continue

    if cross != 2 * edge:
        print(0)
        continue

    print(1)