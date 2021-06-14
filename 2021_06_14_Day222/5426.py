# 1D1P Day222 BOJ 5426번 비밀 편지 문제 - 2021.06.14

for tc in range(1, int(input())+1):

    string = input()

    size = int(len(string) ** 0.5)

    box = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(size):
        for j in range(size):
            box[i][j] = string[size*i + j]
    
    answer = ''
    for i in range(size):
        for j in range(size):
            answer += box[j][size-1-i]
    
    print(answer)