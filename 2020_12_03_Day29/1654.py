# 1D1P Day29 BOJ 1654번 랜선 자르기 문제 - 2020.12.03

from sys import stdin

K, N = map(int, stdin.readline().rstrip().split(' '))

cables = [0] * K

for i in range(K):
    cables[i] = int(stdin.readline().rstrip())

cables.sort(reverse = True)

left = 0
right = cables[0]
maximum = 0

def howmanycables(cables, mid):

    result = 0
    for i in range(K):
        tmp = cables[i]
        result += int(tmp / mid)
    
    return result

while left <= right:
    
    mid = int((left + right) / 2)
    if mid == 0:
        mid = 1
    
    if howmanycables(cables, mid) >= N:
        left = mid + 1
    
    else:
        right = mid - 1

print(left - 1)