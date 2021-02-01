# 1D1P Day89 SWEA 1215번 회문1 문제 - 2021.02.01

for t in range(1, 11):
    N = int(input())
    string = []
    for _ in range(8):
        string.append(input())

    def doit(string):
        answer = 0
        for i in range(8):
            for j in range(8-N+1):
                tmp = string[i][j:j+N]
                if tmp == tmp[::-1]:
                    answer += 1
        return answer
    
    result = 0

    result += doit(string)

    transposed_string = []
    for i in range(8):
        tmp = ""
        for j in range(8):
            tmp += string[j][i]
        transposed_string.append(tmp)
    
    result += doit(transposed_string)

    print(f"#{t} {result}")