# 1D1P Day211 BOJ 15722번 빙글빙글 스네일 문제 - 2021.06.03

direction = 0
x, y = 0, 0
many = 1
N = int(input())
time = 0

while time != N:
    for i in range(2):
        for j in range(many):
            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1
            time += 1

            if time == N:
                break
        if time == N:
            break
        direction = (direction + 1) % 4
    many += 1

print(x, y)