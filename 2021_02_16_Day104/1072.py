# 1D1P Day104 BOJ 1072번 게임 문제 - 2021.02.16

import math

X, Y = map(int, input().split())

Z = int(100 * Y / X)
answer = -1
if Z < 99:
    answer = math.ceil(((Z+1)*X - 100*Y) / (99-Z))

print(answer)