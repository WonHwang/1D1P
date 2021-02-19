# 1D1P Day107 JUNGOL 167번 배열2 - 형성평가8 문제 - 2021.02.19

numbers = []
for _ in range(4):
    numbers.append(list(map(int, input().split())))

for i in range(4):
    tmp = 0
    for j in range(2):
        tmp += numbers[i][j]
    
    print(tmp // 2, end = " ")
print()

for i in range(2):
    tmp = 0
    for j in range(4):
        tmp += numbers[j][i]
    
    print(tmp // 4, end = " ")
print()

tmp = 0
for i in range(4):
    for j in range(2):
        tmp += numbers[i][j]

print(tmp // 8)