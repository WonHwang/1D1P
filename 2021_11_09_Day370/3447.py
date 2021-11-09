# 1D1P Day370 BOJ 3447번 버그왕 문제 - 2021.11.09

content = []

while True:
    try:
        content.append(input())
    
    except EOFError:
        break

answer = []
for string in content:
    tmp = string
    while 'BUG' in tmp:
        tmp = tmp.replace('BUG', '')
    answer.append(tmp)

for string in answer:
    print(string)