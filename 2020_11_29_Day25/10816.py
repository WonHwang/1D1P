# 1D1P Day25 BOJ 10816번 숫자 카드 2 문제

import sys

N = int(sys.stdin.readline().rstrip())

numbers = sys.stdin.readline().rstrip().split(' ')

number = dict()
for i in range(N):
    if numbers[i] in number:
        number[numbers[i]] += 1
    else:
        number[numbers[i]] = 1

M = int(sys.stdin.readline().rstrip())
target = sys.stdin.readline().rstrip().split(' ')
answer = ""
for i in range(M):
    if target[i] in number:
        answer += str(number[target[i]]) + " "
    else:
        answer += "0 "

print(answer[:-1])