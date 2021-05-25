# 1D1P Day202 BOJ 9366번 삼각형 분류 문제 - 2021.05.25

def istriangle(a, b, c):

    if a >= b + c:
        return False
    if b >= a + c:
        return False
    if c >= a + b:
        return False
    return True

def det(a, b, c):

    if a == b == c:
        return 'equilateral'
    
    elif (a == b and a != c) or (b == c and a != b) or (c == a and b != c):
        return 'isosceles'
    
    else:
        return 'scalene'

for tc in range(1, int(input())+1):

    a, b, c = map(int, input().split())

    if istriangle(a, b, c):
        print(f"Case #{tc}: {det(a, b, c)}")
    else:
        print(f"Case #{tc}: invalid!")