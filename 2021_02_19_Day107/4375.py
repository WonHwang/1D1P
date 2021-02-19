# 1D1P Day107 BOJ 4375번 1 문제 - 2021.02.19

while True:
    try:
        n = int(input())
        
        digit = 1
        target = 1

        while target % n:
            digit += 1
            target *= 10
            target += 1
        
        print(digit)

    except EOFError:
        break