# 1D1P Day208 BOJ 10101번 삼각형 외우기 문제 - 2021.05.31

def det(a, b, c):
    if a == b == c == 60:
        return 'Equilateral'
    
    elif a + b + c == 180 and (a == b or b == c or c == a):
        return 'Isosceles'
    
    elif a + b + c == 180 and a != b and b != c and c != a:
        return 'Scalene'
    
    else:
        return 'Error'

a = int(input())
b = int(input())
c = int(input())

print(det(a, b, c))