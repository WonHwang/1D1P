# 1D1P Day68 BOJ 3896번 Z 문제 - 2021.01.11

N, r, c = map(int, input().split(' '))

answer = 0

N = 2**N
r += 1
c += 1

while N > 2:
    half = N // 2
    if r <= half and c > half:
        answer += half ** 2
        c -= half
    elif r > half and c <= half:
        answer += 2*(half ** 2)
        r -= half
    elif r > half and c > half:
        answer += 3*(half ** 2)
        r -= half
        c -= half
    N = N // 2

if r == 1 and c == 1:
    answer += 1
elif r == 1 and  c == 2:
    answer += 2
elif r == 2 and c == 1:
    answer += 3
elif r == 2 and c == 2:
    answer += 4

print(answer - 1)