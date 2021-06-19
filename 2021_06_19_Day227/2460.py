# 1D1P Day227 BOJ 2460번 지능형 기차2 문제 - 2021.06.19

Max = 0
man = 0

for _ in range(10):
    o, i = map(int, input().split())
    man -= o
    man += i
    if man > Max:
        Max = man

print(Max)