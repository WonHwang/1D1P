# 1D1P Day193 BOJ 1213번 팰린드롬 만들기 문제 - 2021.05.16

string = input()
alphabets = [0] * 26

for digit in string:
    alphabets[ord(digit) - ord('A')] += 1

front = ""
rear = ""
middle = ""

for i in range(26):
    if alphabets[i] % 2:
        middle += chr(i + ord('A'))
        alphabets[i] -= 1

for i in range(26):
    if not alphabets[i] % 2:
        for j in range(alphabets[i] // 2):
            front += chr(i + ord('A'))
            rear = chr(i + ord('A')) + rear

answer = front + middle + rear

if answer == answer[::-1]:
    print(answer)

else:
    print("I'm Sorry Hansoo")
