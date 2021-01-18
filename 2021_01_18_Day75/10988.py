# 1D1P Day75 BOJ 10988번 팰린드롬인지 확인하기 문제 - 2021.01.18
tmp = input()
print(1 if tmp == tmp[::-1] else 0)