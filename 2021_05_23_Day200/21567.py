# 1D1P Day200 BOJ 21567번 숫자의 개수 2 문제 - 2021.05.23

A = int(input())
B = int(input())
C = int(input())
answer = [0] * 10
result = A*B*C
while result != 0:
    answer[result%10] += 1
    result //= 10

for i in range(10):
    print(answer[i])