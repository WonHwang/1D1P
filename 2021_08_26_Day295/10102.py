# 1D1P Day295 BOJ 10102번 개표 문제 - 2021.08.26

N = int(input())
string = input()
A, B = 0, 0
for i in range(N):
    if string[i] == 'A':
        A += 1
    else:
        B += 1

if A > B:
    print('A')

elif B > A:
    print('B')

else:
    print('Tie')