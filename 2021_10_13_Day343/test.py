# 1D1P Day343 Codility 데모 테스트 문제 - 2021.10.13

def solution(A):
    A = list(set(A))
    A.sort()

    answer = 1
    for num in A:
        if num <= 0:
            continue
        
        if num > answer:
            break
        
        elif num == answer:
            answer += 1
    
    return answer