# 1D1P Day89 SWEA 1216번 회문2 문제 - 2021.02.01

for _ in range(1, 11):
    t = int(input())
    string = []
    for i in range(100):
        string.append(input())
    
    transposed_string = []
    for i in range(100):
        tmp = ""
        for j in range(100):
            tmp += string[j][i]
        transposed_string.append(tmp)
    
    def find(string, n):
        for i in range(100):
            for j in range(100-n+1):
                tmp = string[i][j:j+n]
                if tmp == tmp[::-1]:
                    return n
    
    answer = 0

    for i in range(100, 0, -1):
        if find(string, i):
            print(f"#{t} {i}")
            break
        if find(transposed_string, i):
            print(f"#{t} {i}")
            break