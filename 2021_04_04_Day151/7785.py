# 1D1P Day151 BOJ 7785번 회사에 있는 사람 문제 - 2021.04.04

from sys import stdin
input = stdin.readline

N = int(input())

company = set()

for _ in range(N):
    name, status = map(str, input().split())

    if status == 'enter':
        company.add(name)
    else:
        company.remove(name)

company = list(company)
company.sort(reverse=True)
for name in company:
    print(name)