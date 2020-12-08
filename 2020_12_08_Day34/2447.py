# 1D1P Day34 BOJ 2447번 별 찍기 - 10 문제 - 2020.12.08

N = int(input())

def star(N):
    target = []
    M = N
    while M >= 3:
        target.append(M)
        M = M // 3
    answer = ""
    isit = 0
    for i in range(N):
        for j in range(N):
            for num in target:
                tmp = num // 3
                if (i%num) >= tmp and (i%num) < (2*tmp) and (j%num) >= tmp and (j%num) < (2*tmp):
                    isit = 1
                    break
            if isit:
                answer += " "
                isit = 0
            else:
                answer += '*'
        answer += "\n"
    
    return answer

print(star(N))