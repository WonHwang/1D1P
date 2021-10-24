# 1D1P Day354 BOJ 1547번 공 문제 - 2021.10.24

cups = [0] * 4

cups[1] = 1

for _ in range(int(input())):
    a, b = map(int, input().split())
    cups[a], cups[b] = cups[b], cups[a]

for i in range(1, 4):
    if cups[i]:
        print(i)
        break