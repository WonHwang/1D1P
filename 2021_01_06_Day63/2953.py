# 1D1P Day63 BOJ 2953번 나는 요리사다 문제 - 2021.01.06

maximum, index = 0, -1

for i in range(5):
    tmp = sum(map(int, input().split(' ')))
    if tmp > maximum:
        maximum = tmp
        index = i+1

print(index, maximum)