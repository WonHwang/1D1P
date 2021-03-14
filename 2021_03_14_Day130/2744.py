# 1D1P Day130 BOJ 2744번 대소문자 바꾸기 문제 - 2021.03.14

string = input()
answer = ""
for char in string:
    if ord(char) >= 97:
        answer += chr(ord(char)-32)
    
    else:
        answer += chr(ord(char)+32)
print(answer)