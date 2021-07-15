# 1D1P Day253 BOJ 7567번 그릇 문제 - 2021.07.15

string = input()
last = ''
answer = 0

for cup in string:
    if cup == '(':
        if last == '(':
            answer += 5
        else:
            answer += 10
    elif cup == ')':
        if last == ')':
            answer += 5
        else:
            answer += 10
    last = cup

print(answer)