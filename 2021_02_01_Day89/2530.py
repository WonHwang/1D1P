# 1D1P Day89 BOJ 2530번 인공지능 시계 문제 - 2021.02.01

H, M, S = map(int, input().split())
time = int(input())

tosec = ((H * 60 * 60) + (M * 60) + S + time) % (60 * 60 * 24)

h = tosec // 3600
tosec %= 3600
m = tosec // 60
tosec %= 60
print(f"{h} {m} {tosec}")