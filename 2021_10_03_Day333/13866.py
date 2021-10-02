# 1D1P Day333 BOJ 13866번 팀 나누기 문제 - 2021.10.03

level = list(map(int, input().split()))

answer = sum(level)

for i in range(3):
    for j in range(i+1, 4):
        a, b = level[i], level[j]
        
        tmp =  abs(sum(level) - (a + b) - (a + b))
        if tmp < answer:
            answer = tmp

print(answer)