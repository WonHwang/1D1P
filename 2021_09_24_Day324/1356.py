# 1D1P Day324 BOJ 1356번 유진수 문제 - 2021.09.24

N = input()
answer = 0

for i in range(1, len(N)):
    front = N[:i]
    rear = N[i:]

    Front = 1
    Rear = 1

    for num in front:
        Front *= int(num)
    for num in rear:
        Rear *= int(num)

    if Front == Rear:
        answer = 1
        break

print("YES" if answer else "NO")