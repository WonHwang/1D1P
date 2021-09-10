# 1D1P Day310 BOJ 1251번 단어 나누기 문제 - 2021.09.10

words = []

string = input()

length = len(string)

for i in range(1, length-1):
    for j in range(1, length - i):
        k = length - i - j
        a = string[:i]
        b = string[i:i+j]
        c = string[i+j:i+j+k]
        a = a[::-1]
        b = b[::-1]
        c = c[::-1]
        words.append(a+b+c)

words.sort()
print(words[0])