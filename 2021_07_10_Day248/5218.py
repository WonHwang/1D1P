# 1D1P Day248 BOJ 5218번 알파벳 거리 문제 - 2021.07.10

def alphabetdistance(c):
    return ord(c) - ord('A') + 1

for _ in range(int(input())):
    A, B = map(str, input().split())
    
    answers = []
    for i in range(len(A)):
        x, y = alphabetdistance(A[i]), alphabetdistance(B[i])
        
        if x > y:
            answer = y + 26 - x
        else:
            answer = y - x
        answers.append(answer)
    
    print("Distances: ", end="")
    print(*answers)