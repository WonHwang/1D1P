# 1D1P Day165 BOJ 5635번 생일 문제 - 2021.04.18

N = int(input())

people = []

date = [[[[] for _ in range(31)] for _ in range(12)] for _ in range(22)]

for _ in range(N):
    name, day, month, year = map(str, input().split())
    date[int(year)-1990][int(month)-1][int(day)-1].append(name)

flag = 0
for i in range(22):
    for j in range(12):
        for k in range(31):
            if date[21-i][11-j][30-k]:
                print(date[21-i][11-j][30-k][0])
                flag = 1
                break
        if flag:
            break
    if flag:
        break

flag = 0
for i in range(22):
    for j in range(12):
        for k in range(31):
            if date[i][j][k]:
                print(date[i][j][k][0])
                flag = 1
                break
        if flag:
            break
    if flag:
        break