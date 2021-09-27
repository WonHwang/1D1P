# 1D1P Day327 BOJ 1718번 암호 문제 - 2021.09.27

plain = input()
key = input()

crypt = ''

for i in range(len(plain)):
    if 'a' <= plain[i] <= 'z':
        
        crypt += chr(((ord(plain[i]) - ord(key[i % len(key)]) - 1) % 26) + ord('a'))
    
    else:
        crypt += plain[i]

print(crypt)