# 1D1P Day13 BOJ 10833번 사과 문제 - 2020.11.17

N = int(input())
answer = 0
for i in range(N):
    students , apples = map(int, input().split(' '))
    answer += (apples % students)
print(answer)