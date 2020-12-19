# 1D1P Day45 BOJ 1550번 16진수 문제 - 2020.12.19

N = input()

answer = 0

for i in range(len(N)):
    tmp = N[i]
    if ord(tmp) >= 65:
        answer = (16 * answer) + (ord(tmp) - 55)
    else:
        answer = (16 * answer) + int(tmp)

print(answer)