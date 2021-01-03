# 1D1P Day60 BOJ 5086번 배수와 약수 문제 - 2021.01.03

while True:
    a, b = map(int, input().split(' '))

    if a == 0 and b == 0:
        break

    if a % b == 0:
        print('multiple')
    
    elif b % a == 0:
        print('factor')
    
    else:
        print('neither')