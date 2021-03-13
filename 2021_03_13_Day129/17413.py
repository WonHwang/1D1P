# 1D1P Day129 BOJ 17413번 단어 뒤집기 2 문제 - 2021.03.13

from collections import deque

string = list(input())
queue = deque(string)

answer = ""
tmp = ""
while queue:
    char = queue.popleft()

    if char == '<':
        answer += tmp[::-1]
        tmp = "<"

        while True:
            char = queue.popleft()
            tmp += char
            if char == '>':
                answer += tmp
                tmp = ""
                break
    
    elif char == ' ':
        answer += tmp[::-1]
        answer += " "
        tmp = ""
    
    else:
        tmp += char

answer += tmp[::-1]

print(answer)