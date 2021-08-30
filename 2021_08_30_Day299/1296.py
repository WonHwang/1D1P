# 1D1P Day299 BOJ 1296번 데이트 문제 - 2021.08.30

name = input()
N = int(input())
names = []

for _ in range(N):
    names.append(input())

names.sort()

score = -1
answer = ''

digits = [0, 0, 0, 0]
for digit in name:
    if digit == 'L':
        digits[0] += 1
    elif digit == 'O':
        digits[1] += 1
    elif digit == 'V':
        digits[2] += 1
    elif digit == 'E':
        digits[3] += 1

for i in range(N):
    tmp = digits[:]

    for digit in names[i]:
        if digit == 'L':
            tmp[0] += 1
        elif digit == 'O':
            tmp[1] += 1
        elif digit == 'V':
            tmp[2] += 1
        elif digit == 'E':
            tmp[3] += 1
    
    tmp_score = ((tmp[0] + tmp[1]) * (tmp[0] + tmp[2]) * (tmp[0] + tmp[3]) * (tmp[1] + tmp[2]) * (tmp[1] + tmp[3]) * (tmp[2] + tmp[3])) % 100

    if tmp_score > score:
        score = tmp_score
        answer = names[i]

print(answer)