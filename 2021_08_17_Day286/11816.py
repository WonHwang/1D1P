# 1D1P Day286 BOJ 11816번 8진수, 10진수, 16진수 문제 - 2021.08.17

N = input()

if N[:2] == '0x':
    answer = int(N, 16)

elif N[:1] == '0':
    answer = int('0o' + N[1:], 8)

else:
    answer = int(N)

print(answer)