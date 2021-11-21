# 1D1P Day373 BOJ 2993번 세 부분 문제 - 2021.11.21

word = input()
answer = 'z' * len(word)\

for i in range(1, len(word)-1):
    for j in range(1, len(word)-i):
        first = word[:i]
        second = word[i:i+j]
        third = word[i+j:]

        tmp = first[::-1] + second[::-1] + third[::-1]

        if tmp < answer:
            answer = tmp

print(answer)