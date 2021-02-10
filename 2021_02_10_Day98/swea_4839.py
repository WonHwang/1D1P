# 1D1P Day98 SWEA 4839번 이진탐색 문제 - 2021.02.10

for tc in range(1, int(input()) + 1):
    P, A, B = map(int, input().split())


    def binarysearch(P, target):
        l, r = 1, P

        count = 0
        while True:
            count += 1
            mid = (l + r) // 2
            
            if mid == target:
                break

            if target > mid:
                l = mid
            else:
                r = mid
        
        return count
    
    a = binarysearch(P, A)
    b = binarysearch(P, B)

    print(f"#{tc}", end = ' ')

    if a < b:
        print('A')
    elif a == b:
        print(0)
    else:
        print('B')