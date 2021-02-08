N = int(input())

students = list(map(int, input().split()))

B, C = map(int, input().split())
answer = 0

for i in range(N):
    students[i] -= B
    answer += 1
    if students[i] > 0:
        answer += (students[i] // C)
        students[i] %= C
        if students[i]:
            answer += 1

print(answer)