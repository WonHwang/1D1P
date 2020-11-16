# 1D1P Day12 BOJ 2004번 조합 0의 개수 문제 - 2020.11.16

N, M = map(int, input().split(' '))

numof2 = 0
numof5 = 0

tmp = N
while tmp > 0:
    numof2 += int(tmp/2)
    tmp = int(tmp/2)

tmp = N
while tmp > 0:
    numof5 += int(tmp/5)
    tmp = int(tmp/5)

tmp = N-M
while tmp > 0:
    numof2 -= int(tmp/2)
    tmp = int(tmp/2)

tmp = N-M
while tmp > 0:
    numof5 -= int(tmp/5)
    tmp = int(tmp/5)

tmp = M
while tmp > 0:
    numof2 -= int(tmp/2)
    tmp = int(tmp/2)

tmp = M
while tmp > 0:
    numof5 -= int(tmp/5)
    tmp = int(tmp/5)

answer = numof2
if answer > numof5:
    answer = numof5

print(answer)