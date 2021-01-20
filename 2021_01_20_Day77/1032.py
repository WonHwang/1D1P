# 1D1P Day77 BOJ 1032번 명령 프롬프트 문제 - 2021.01.20

strings = []
N = int(input())
for i in range(N):
    strings.append(input())

answer = ""
for i in range(len(strings[0])):
    tmp = strings[0][i]
    for string in strings:
        if string[i] != tmp:
            answer += '?'
            break
    else:
        answer += tmp

print(answer)