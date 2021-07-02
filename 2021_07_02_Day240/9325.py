# 1D1P Day240 BOJ 9325번 얼마? 문제 - 2021.07.02

from sys import stdin
input = stdin.readline

for tc in range(int(input())):
    answer = int(input())
    for op in range(int(input())):
        cnt, price = map(int, input().split())
        answer += cnt * price
    print(answer)