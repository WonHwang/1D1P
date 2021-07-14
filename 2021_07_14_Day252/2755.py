# 1D1P Day252 BOJ 2755번 이번학기 평점은 몇점? 문제 - 2021.07.14

from sys import stdin
import decimal
input = stdin.readline

grade = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}

N = int(input())

total = 0
cnt = 0

for _ in range(N):
    name, time, grd = map(str, input().split())
    cnt += int(time)
    total += int(time) * grade[grd]

print(round(decimal.Decimal(str(total/cnt)), 2))