# 1D1P Day79 SWEA 1966번 숫자를 정렬하자 문제 - 2021.01.22

for _ in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"#{_}", end = " ")
    for i in range(N):
        print(arr[i], end = " ")
    print()