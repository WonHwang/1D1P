# 1D1P Day25 BOJ 1620번 나는야 포켓몬 마스터 이다솜 문제 - 2020.11.29

import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

name_dict = dict()
number_dict = dict()

for i in range(1, N+1):
    name = sys.stdin.readline().rstrip()
    name_dict[name] = i
    number_dict[i] = name

for i in range(M):
    input_ = sys.stdin.readline().rstrip()
    if ord(input_[0]) >= 48 and ord(input_[0]) <= 57:
        print(number_dict[int(input_)])
    else:
        print(name_dict[input_])