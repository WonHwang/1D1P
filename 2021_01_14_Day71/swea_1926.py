# 1D1P Day71 SWEA 1926번 간단한 369게임 문제 - 2021.01.14

N = int(input())
answer = ""


def has3(num):
    result = 0
    while num != 0:
        if num % 10 == 3 or num % 10 == 6 or num % 10 == 9:
            result += 1
            num //= 10
        else:
            num //= 10
    return result

for i in range(1, N+1):
    tmp = has3(i)
    if tmp:
        answer += '-' * tmp
    else:
        answer += str(i)
    answer += ' '

print(answer[:-1])