# 1D1P Day194 BOJ 2776번 암기왕 문제 - 2021.05.17

for tc in range(int(input())):
    N = int(input())
    nums1 = set(list(map(int, input().split())))
    
    M = int(input())
    nums2 = list(map(int, input().split()))
    for num in nums2:
        if num in nums1:
            print(1)
        else:
            print(0)