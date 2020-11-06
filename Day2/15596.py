# 1D1P Day2 BOJ 15596번 정수 N개의 합 문제 - 2020.11.06

def solve(a):
    length = len(a)
    answer = 0
    for i in range(length):
        answer += a[i]
    
    return answer