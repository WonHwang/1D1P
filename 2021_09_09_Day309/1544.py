# 1D1P Day309 BOJ 1544번 사이클 단어 문제 - 2021.09.09

words = []

for _ in range(int(input())):

    string = input()

    for i in range(len(string)):
        tmp = string[i:] + string[:i]
        if tmp in words:
            break
    else:
        words.append(string)

print(len(words))