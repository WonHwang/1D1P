# 1D1P Day198 BOJ 12813번 이진수 연산 문제 - 2021.05.21

A = input()
B = input()

result = ""
for i in range(len(A)):
    if A[i] == '1' and B[i] == '1':
        result += '1'
    else:
        result += '0'
print(result)

result = ""
for i in range(len(A)):
    if A[i] == '1' or B[i] == '1':
        result += '1'
    else:
        result += '0'

print(result)

result = ""
for i in range(len(A)):
    if A[i] == B[i]:
        result += '0'
    else:
        result += '1'
print(result)

result = ""
for i in range(len(A)):
    if A[i] == '1':
        result += '0'
    else:
        result += '1'
print(result)

result = ""
for i in range(len(B)):
    if B[i] == '1':
        result += '0'
    else:
        result += '1'
print(result)