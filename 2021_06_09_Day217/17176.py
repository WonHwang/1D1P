# 1D1P Day217 BOJ 17176번 암호해독기 문제 - 2021.06.09

from sys import stdin
input = stdin.readline

N = int(input())
C = list(map(int, input().split()))
P = input().rstrip()
D = ''

P_dict = dict()
P_dict[' '] = 0
for i in range(26):
    P_dict[chr(ord('A') + i)] = 0
    P_dict[chr(ord('a') + i)] = 0

for digit in P:
    P_dict[digit] += 1

for num in C:
    if num == 0:
        D += ' '
    elif 1 <= num <= 26:
        D += chr(num - 1 + ord('A'))
    elif 27 <= num <= 52:
        D += chr(num - 27 + ord('a'))

for digit in D:
    P_dict[digit] -= 1

answer = 'y'
for digit in P_dict:
    if P_dict[digit] != 0:
        answer = 'n'
        break

print(answer)