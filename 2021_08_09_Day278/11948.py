# 1D1P Day278 BOJ 11948번 과목선택 문제 - 2021.08.09

A = []
B = []
for _ in range(4):
    A.append(int(input()))

for _ in range(2):
    B.append(int(input()))

A.sort()
B.sort()
answer = 0
for i in range(3):
    answer += A[3-i]

answer += B[1]

print(answer)