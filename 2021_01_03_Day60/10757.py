# 1D1P Day60 BOJ 10757번 큰 수 A+B 문제 - 2021.01.03

def summation(A, B):
    A, B = A[::-1], B[::-1]
    length = len(A)
    if length < len(B):
        length = len(B)
    
    while len(A) < length:
        A += '0'
    
    while len(B) < length:
        B += '0'
    
    carry = 0
    answer = ""
    for i in range(length):
        tmp = carry + ord(A[i]) - 48 + ord(B[i]) - 48
        digit = tmp % 10
        carry = tmp // 10
        answer += str(digit)
    if carry != 0:
        answer += str(carry)
    
    return answer




A, B = input().split(' ')
print(summation(A, B)[::-1])