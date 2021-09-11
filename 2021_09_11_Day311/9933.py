# 1D1P Day311 BOJ 9933번 민균이의 비밀번호 문제 - 2021.09.11

words = {}

for _ in range(int(input())):
    word = input()
    words[word] = 1
    if words.get(word[::-1]):
        answer = word
    
print(len(answer), answer[len(answer)//2])