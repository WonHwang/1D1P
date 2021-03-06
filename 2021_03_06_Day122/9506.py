# 1D1P Day112 BOJ 9506번 약수들의 합 문제 - 2021.03.06

while True:
    n = int(input())
    if n == -1:
        break
    tmp = 0
    for i in range(1, n):
        if not n%i:
            tmp += i
    if tmp == n:
        answer = f"{n} = "
        for i in range(1, n):
            if not n%i:
                answer += str(i) + ' + '
        answer = answer[:-2]
    else:
        answer = f"{n} is NOT perfect."
    
    print(answer)