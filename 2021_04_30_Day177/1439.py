# 1D1P Day177 BOJ 1439번 뒤집기 문제 - 2021.04.30

string = input()

zeros = 0
for zero in string.split('1'):
    if zero:
        zeros += 1

ones = 0
for one in string.split('0'):
    if one:
        ones += 1

print(zeros if zeros < ones else ones)