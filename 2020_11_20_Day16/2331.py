# 1D1P Day16 BOJ - 2331번 반복수열 문제 - 2020.11.20

A, P = map(int, input().split(' '))

def makeD(number, P):
    answer = 0
    while number != 0:
        answer += (number % 10) ** P
        number = int(number/10)
    return answer

D = [0] * 236196
D[0] = A

for i in range(236195):
    D[i+1] = makeD(D[i], P)

answer = -1
for i in range(236195):
    for j in range(i+1, 236196):
        if D[i] == D[j]:
            answer = i
            break
    if answer == i:
        break

answer = D[:answer]

print(len(answer))