# 1D1P Day187 BOJ 6571번 피보나치 수의 개수 문제 - 2021.05.10

a, b = 1, 1
c = 1
idx = 2
result = {1: 1, 2: 2}
while c <= 10**100:
    c = a + b
    result[idx] = c
    idx += 1
    a, b = b, c

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break

    for i in range(1, 500):
        if result[i] > b:
            end = i - 1
            break
    
    for i in range(1, 500):
        if result[i] >= a:
            start = i - 1
            break

    print(end - start)