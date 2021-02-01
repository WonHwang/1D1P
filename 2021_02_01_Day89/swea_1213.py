# 1D1P Day89 SWEA 1213번 String 문제 - 2021.02.01

for _ in range(10):
    t = int(input())
    target = input()
    string = input()
    string = string.split(target)
    print(f"#{t} {len(string)-1}")