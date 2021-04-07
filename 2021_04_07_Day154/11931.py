# 1D1P Day154 BOJ 11931번 수 정렬하기 4 문제 - 2021.04.07

from sys import stdin
input = stdin.readline

N = int(input())
numbers = [0] * 2000001
for _ in range(N):
    number = int(input())
    if number < 0:
        numbers[1000000 - number] += 1
    else:
        numbers[number] += 1

for i in range(1000000, -1, -1):
    if numbers[i]:
        for j in range(numbers[i]):
            print(i)

for i in range(1000001, 2000001):
    if numbers[i]:
        for j in range(numbers[i]):
            print(1000000 - i)