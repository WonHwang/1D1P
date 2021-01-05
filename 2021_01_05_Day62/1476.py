# 1D1P Day62 BOJ 1476번 날짜 계산 문제 - 2021.01.05

E, S, M = map(int, input().split(' '))

e, s, m, years = 1, 1, 1, 1

while True:
    if e == E and s == S and m == M:
        break
    e = (e + 1) % 16
    if e == 0:
        e += 1
    s = (s + 1) % 29
    if s == 0:
        s += 1
    m = (m + 1) % 20
    if m == 0:
        m += 1
    years += 1

print(years)