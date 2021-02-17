# 1D1P Day105 BOJ 11365번 !비밀 급일 문제 - 2021.02.17

import sys
input = sys.stdin.readline

while True:
    tmp = input().rstrip()
    if tmp == 'END':
        break
    print(tmp[::-1])