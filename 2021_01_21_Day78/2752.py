# 1D1P Day78 BOJ 2752번 세수 정렬 문제 - 2021.01.21

def sesusort(A, B, C):
    if A >= B:
        if B >= C:
            print(C, B, A)
        else:
            if A >= C:
                print(B, C, A)
            else:
                print(B, A, C)
    else:
        if A >= C:
            print(C, A, B)
        else:
            if B >= C:
                print(A, C, B)
            else:
                print(A, B, C)
A, B, C = map(int, input().split(' '))
sesusort(A, B, C)