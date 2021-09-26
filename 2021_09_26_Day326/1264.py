# 1D1P Day326 BOJ 1264번 모음의 개수 문제 - 2021.09.26

vowel = {'a', 'e', 'i', 'o', 'u'}

while True:
    string = input().lower()

    if string == '#':
        break
    
    cnt = 0
    for char in string:
        if char in vowel:
            cnt += 1
    
    print(cnt)