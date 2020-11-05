# 1D1P Day1 BOJ 11005번 진법 변환 2 문제 - 2020.11.05

input_ = input().split(' ')
N, B = int(input_[0]), int(input_[1])
result = ""

while N != 0:
    digit = N % B
    N = int(N/B)
    if digit >= 10:
        digit += 55
        digit = chr(digit)
    else:
        digit = str(digit)
    result  = digit + result

print(result)