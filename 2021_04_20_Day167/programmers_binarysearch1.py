# 1D1P Day167 programmers 이분탐색 1번 입국심사 문제 - 2021.04.20

n = 8
times = [3, 7, 12]

def solution(n, times):

    start, end = 1, 1000000000 ** 2

    while start < end:
        mid = (start + end) // 2

        tmp = 0
        for time in times:
            tmp += mid // time
        
        if tmp >= n:
            end = mid
        
        else:
            start = mid + 1

    return start

print(solution(n, times))