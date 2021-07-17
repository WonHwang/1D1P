# 1D1P Day255 BOJ 2789번 유학 금지 문제 - 2021.07.17

string = list(input())
for i in range(len(string)):
    if string[i] in "CAMBRIDGE":
        string[i] = ''
print(''.join(string))