# 1D1P Day31 BOJ 2110번 공유기 설치 문제 - 2020.12.05

from sys import stdin

N, C = map(int, stdin.readline().rstrip().split(' '))

house = []

for _ in range(N):
    house.append(int(stdin.readline().rstrip()))

house.sort()

def setwifi(gap):
    result = 1
    previous = house[0]
    for i in range(N-1):
        if (house[i+1] - previous) >= gap:
            result += 1
            previous = house[i+1]
    
    return result

front = 1
end = house[-1] - house[0]
result = 0

while front <= end:
    mid = (front + end) // 2

    if setwifi(mid) >= C:
        result = max(result, mid)
        front = mid + 1
    
    else:
        end = mid - 1
    
    

print(result)