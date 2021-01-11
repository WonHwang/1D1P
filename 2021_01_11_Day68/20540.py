# 1D1P Day68 BOJ 20540번 연길이의 이상형 문제 - 2021.01.11

tmp = input()

answer = ""
if tmp[0] == 'E':
    answer += "I"
else:
    answer += "E"
if tmp[1] == 'S':
    answer += 'N'
else:
    answer += "S"
if tmp[2] == 'F':
    answer += 'T'
else:
    answer += 'F'
if tmp[3] == 'J':
    answer += 'P'
else:
    answer += 'J'
print(answer)