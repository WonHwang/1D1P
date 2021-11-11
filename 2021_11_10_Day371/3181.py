# 1D1P Day371 BOJ 3181번 줄임말 만들기 문제 - 2021.11.10

ignore = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
words = list(input().split())

answer = ''
for i in range(len(words)):
    if words[i] not in ignore:
        answer += words[i][0].upper()
    
    else:
        if i == 0:
            answer += words[i][0].upper()

print(answer)