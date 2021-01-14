# 1D1P Day71 BOJ 9093번 단어 뒤집기 문제 - 2021.01.14
from sys import stdin

T = int(stdin.readline().rstrip())

for _ in range(T):
    string = stdin.readline().rstrip()[::-1].split(' ')[::-1]
    answer = ""
    for word in string:
        answer += word + " "
    print(answer[:-1])