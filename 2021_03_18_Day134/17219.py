# 1D1P Day134 BOJ 17219번 비밀번호 찾기 문제 - 2021.03.18

from sys import stdin
input = stdin.readline

N, M = map(int, input().rstrip().split())

password = dict()

for _ in range(N):
    
    site, pw = map(str, input().rstrip().split())
    password[site] = pw

for _ in range(M):

    target = input().rstrip()
    print(password[target])