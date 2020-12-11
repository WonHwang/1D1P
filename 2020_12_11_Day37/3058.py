# 1D1P Day37 BOJ 3058번 짝수를 찾아라 문제 - 2020.12.11
# 면접 이후로 공부가 영 안되네

T = int(input())

for _ in range(T):
    arr = input().split(' ')
    total = 0
    minimum = 100
    for i in range(7):
        tmp = int(arr[i])
        if tmp % 2 == 0:
            total += tmp
            if minimum > tmp:
                minimum = tmp
    
    print(total, minimum)