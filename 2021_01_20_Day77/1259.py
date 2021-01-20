# 1D1P Day77 BOJ 1259번 팰린드롬 수 문제 - 2021.01.20

while True:
    number = input()
    if number == '0':
        break

    if number == number[::-1]:
        print("yes")
    else:
        print("no")