# 1D1P Day215 BOJ 7600번 문자가 몇갤까 문제 - 2021.06.07

while True:

    string = input()

    if string == '#':
        break

    alphabets = [0] * 26

    for digit in string:
        if ord('a') <= ord(digit) <= ord('z'):
            alphabets[ord(digit) - ord('a')] = 1
        
        elif ord('A') <= ord(digit) <= ord('Z'):
            alphabets[ord(digit) - ord('A')] = 1
    
    print(sum(alphabets))