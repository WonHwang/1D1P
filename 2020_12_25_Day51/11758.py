# 1D1P Day51 BOJ 11758번 CCW 문제 - 2020.12.25
# 크리스마스 때문에 늦게 올립니다...

x1, y1 = map(int, input().split(' '))
x2, y2 = map(int, input().split(' '))
x3, y3 = map(int, input().split(' '))

if x3 - x1 > 0:
    if y2 > round(((y1 - y3) / (x1 - x3)) * (x2 - x1) + y1, 2):
        print(-1)
    
    elif y2 == round(((y1 - y3) / (x1 - x3)) * (x2 - x1) + y1, 2):
        print(0)
    
    else:
        print(1)

elif x3 - x1 == 0:
    if y3 - y1 > 0:
        if x2 < x1:
            print(-1)

        elif x2 == x1:
            print(0)

        else:
            print(1)
    
    else:
        if x2 > x1:
            print(-1)
        
        elif x2 == x1:
            print(0)
        
        else:
            print(1)

else:
    if y2 < round(((y1 - y3) / (x1 - x3)) * (x2 - x1) + y1, 2):
        print(-1)
    
    elif y2 == round(((y1 - y3) / (x1 - x3)) * (x2 - x1) + y1, 2):
        print(0)
    
    else:
        print(1)
