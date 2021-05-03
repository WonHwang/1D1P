# 1D1P Day180 BOJ 1431번 시리얼 번호 문제 - 2021.05.03

from sys import stdin
input = stdin.readline

def issmaller(a, b):

    if len(a) < len(b):
        return True
    
    elif len(a) > len(b):
        return False
    
    elif len(a) == len(b):
        total_a = 0
        for digit in a:
            if digit.isnumeric():
                total_a += int(digit)
        
        total_b = 0
        for digit in b:
            if digit.isnumeric():
                total_b += int(digit)
        
        if total_a < total_b:
            return True
        
        elif total_a > total_b:
            return False
        
        elif total_a == total_b:
            if a < b:
                return True
            
            elif a > b:
                return False


N = int(input())
strings = []
for _ in range(N):
    strings.append(input().rstrip())

for i in range(N):
    for j in range(N-i-1):
        if issmaller(strings[j+1], strings[j]):
            strings[j], strings[j+1] = strings[j+1], strings[j]

for i in range(N):
    print(strings[i])