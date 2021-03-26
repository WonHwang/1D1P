# 1D1P Day142 BOJ 13706번 제곱근 문제 - 2021.03.26

N = int(input())

start = 1
end = N

while start <= end:
    mid = (start + end) // 2
    
    if N == mid ** 2:
        break

    if N > mid ** 2:
        start = mid + 1
    
    elif N < mid ** 2:
        end = mid - 1
    
print(mid)