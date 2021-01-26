# 1D1P Day83 BOJ 1490번 자리수로 나누기 문제 - 2021.01.26

N = int(input())

def lcm(x, y):
    a, b = x, y
    while b != 0:
        a, b = b, a % b
    return x * y // a

def N_lcm(N):
    answer = 1
    while N != 0:
        tmp = N % 10
        if tmp != 0:
            answer = lcm(answer, tmp)
        N //= 10
    return answer

digit_lcm = N_lcm(N)
digit = 0

do = True

if not N % digit_lcm:
    do = False
    print(N)

while do:
    if digit == 0:
        digit += 1
        continue
    for i in range(10 ** digit):
        tmp = int(str(N) + str(i).zfill(digit))
        if not tmp % digit_lcm:
            do = False
            print(tmp)
            break
    digit += 1