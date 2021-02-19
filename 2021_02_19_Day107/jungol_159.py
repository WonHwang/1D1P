# 1D1P Day107 JUNGOL 159번 배열1 - 형성평가A 문제 - 2021.02.19

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()
numbers.reverse()

for num in numbers:
    print(num)