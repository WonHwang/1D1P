# 1D1P Day204 BOJ 4458번 첫 글자를 대문자로 문제 - 2021.05.27

from sys import stdin
input = stdin.readline

N = int(input())
for _ in range(N):
    string = input().rstrip()
    if ord('a') <= ord(string[0]) <= ord('z'):
        string = chr(ord(string[0]) - 32) + string[1:]
    
    print(string)