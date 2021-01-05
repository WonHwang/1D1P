# 1D1P Day62 BOJ 2576번 홀수 문제 - 2021.01.05

result = 0
minimum = 100

for i in range(7):
    tmp = int(input())
    if tmp % 2 == 1:
        result += tmp
        if tmp < minimum:
            minimum = tmp
if result == 0:
    result = -1
print(result)
if result != -1:
    print(minimum)