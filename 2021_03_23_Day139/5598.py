# 1D1P Day139 BOJ 5598번 카이사르 암호 문제 - 2021.03.23

string = input()
answer = ""
for char in string:
    answer += chr(((ord(char) - ord('A') - 3) % 26) + ord('A'))

print(answer)