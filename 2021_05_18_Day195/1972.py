# 1D1P Day195 BOJ 1972번 놀라운 문자열 문제 - 2021.05.18

while True:
    string = input()
    if string == '*':
        break
    N = len(string)

    answer = 1
    for i in range(1, N):
        D_set = set()
        for j in range(N-i):
            tmp = string[j] + string[j+i]
            if tmp in D_set:
                answer = 0
                break
            D_set.add(tmp)
        if not answer:
            break

    if answer:
        print(f"{string} is surprising.")
    else:
        print(f"{string} is NOT surprising.")