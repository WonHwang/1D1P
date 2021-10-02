# 1D1P Day332 BOJ 15873번 공백 없는 A+B 문제 - 2021.10.02

number = input()
A = int(number[0])
B = int(number[1:])
if number[1] == '0':
    A = int(number[:2])
    B = int(number[2:])
    
print(A + B)