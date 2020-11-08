# 1D1P Day4 BOJ 2745번 진법 변환 문제 - 2020.11.08

input_ = input().split(' ')
number = input_[0]
K = int(input_[1])

answer = 0

for digit in number:
    if digit >= '0' and digit <= '9':
        answer += int(digit)
        answer *= K
    elif digit >= 'A' and digit <= 'Z':
        answer += ord(digit) - 55
        answer *= K

answer = int(answer / K)

print(answer)