# 1D1P Day156 BOJ 1302번 베스트셀러 문제 - 2021.04.09

from sys import stdin
input = stdin.readline

N = int(input())
dic = dict()
for _ in range(N):
    tmp = input().rstrip()
    dic[tmp] = dic.get(tmp, 0) + 1

Max = max(dic.values())

answer = []
for d in dic:
    if dic[d] == Max:
        answer.append(d)

answer.sort()
print(answer[0])