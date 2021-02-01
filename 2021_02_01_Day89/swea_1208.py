# 1D1P Day89 SWEA 1208번 Flatten 문제 - 2021.02.01

for t in range(1, 11):
    N = int(input())
    sand = list(map(int, input().split()))
    for i in range(N):
        maxi = max(sand)
        mini = min(sand)
        max_idx = sand.index(maxi)
        min_idx = sand.index(mini)
        sand[max_idx] -= 1
        sand[min_idx] += 1
    maxi = max(sand)
    mini = min(sand)
    max_idx = sand.index(maxi)
    min_idx = sand.index(mini)
    print(f"#{t} {sand[max_idx] - sand[min_idx]}")