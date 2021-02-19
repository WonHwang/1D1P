# 1D1P Day107 JUNGOL 161번 배열2 - 형성평가2 문제 - 2021.02.19

numbers = list(map(int, input().split()))

number_dict = {}
for i in range(11):
    number_dict[i*10] = 0

for num in numbers:
    if num:
        number_dict[(num // 10) * 10] += 1

for i in range(100, -1, -10):
    if number_dict[i]:
        print(f"{i} : {number_dict[i]} person")