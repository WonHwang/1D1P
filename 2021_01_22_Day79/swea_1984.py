# 1D1P Day79 SWEA 1984번 중간 평균값 구하기 - 2021.01.22

for _ in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{_} {round(sum(arr[1:-1]) / 8)}")