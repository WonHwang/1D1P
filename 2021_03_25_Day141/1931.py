# 1D1P Day141 BOJ 1931번 회의실 배정 문제 - 2021.03.25

from sys import stdin
input = stdin.readline

N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, input().rstrip().split())))

times.sort(key=lambda x:(x[1], x[0]))

answer = 0
end = 0
for time in times:
    if time[0] >= end:
        end = time[1]
        answer += 1

print(answer)