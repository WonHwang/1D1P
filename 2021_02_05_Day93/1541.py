# 1D1P Day93 BOJ 1541번 잃어버린 괄호 문제 - 2021.02.05

string = input().split('-')
numbers = []
for s in string:
    if '+' in s:
        tmp = s.split('+')
        num = 0
        for t in tmp:
            num += int(t)
        numbers.append(num)
    else:
        numbers.append(int(s))

answer = numbers[0]
numbers.pop(0)
for number in numbers:
    answer -= number

print(answer)