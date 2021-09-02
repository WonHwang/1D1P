# 1D1P Day302 BOJ 10768번 특별한 날 문제 - 2021.09.02

def solution(M, D):

    if M < 2:
        return 'Before'
    
    elif M > 2:
        return 'After'
    
    else:
        if D < 18:
            return 'Before'
        
        elif D > 18:
            return 'After'
        
        else:
            return 'Special'

M = int(input())
D = int(input())

print(solution(M, D))