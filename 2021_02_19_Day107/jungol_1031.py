# 1D1P Day107 JUNGOL 1031번 빙고 문제 - 2021.02.19

def isbingo(numbers):
    answer = 0
    for i in range(5):
        tmp = 0
        for j in range(5):
            if numbers[i][j] == 0:
                tmp += 1
        if tmp == 5:
            answer += 1
    
    for i in range(5):
        tmp = 0
        for j in range(5):
            if numbers[j][i] == 0:
                tmp += 1
        if tmp == 5:
            answer += 1
    
    tmp = 0
    for i in range(5):
        if numbers[i][i] == 0:
            tmp += 1
    
    if tmp == 5:
        answer += 1
    
    tmp = 0
    for i in range(5):
        if numbers[i][4-i] == 0:
            tmp += 1
    
    if tmp == 5:
        answer += 1
    
    return answer


numbers = []
for _ in range(5):
    numbers.append(list(map(int, input().split())))

num_dict = {}
for i in range(5):
    for j in range(5):
        num_dict[numbers[i][j]] = [i, j]

target = []
for _ in range(5):
    target.append(list(map(int, input().split())))

tmp = 1
answer = 0
for i in range(5):
    for j in range(5):
        info = num_dict[target[i][j]]
        x, y = info[0], info[1]
        numbers[x][y] = 0
        if isbingo(numbers) >= 3:
            answer = tmp
            break
        tmp += 1
    if answer:
        break

print(answer)