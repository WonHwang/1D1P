# 1D1P Day1 BOJ 9513번 GCD 합 문제 - 2020.11.05
''' 패스한 코드 #1
from math import gcd

N = int(input())

for i in range(N):
    input_ = input().split(' ')
    K = int(input_[0])
    numbers = input_[1:]
    for j in range(K):
        numbers[j] = int(numbers[j])
    
    answer = 0
    for j in range(K):
        for k in range(j+1, K):
            answer += gcd(numbers[j], numbers[k])
    
    print(answer)
'''
# gcd 함수 직접 구현

def gcd(a, b):

    result = 1
    
    if a < b:
        tmp = a
        a = b
        b = tmp
    
    while True:
        res = a % b
        if res == 0:
            result = b
            break
        a = b
        b = res
    
    return result

N = int(input())

for i in range(N):
    input_ = input().split(' ')
    K = int(input_[0])
    numbers = input_[1:]
    for j in range(K):
        numbers[j] = int(numbers[j])
    
    answer = 0
    for j in range(K):
        for k in range(j+1, K):
            answer += gcd(numbers[j], numbers[k])
    
    print(answer)