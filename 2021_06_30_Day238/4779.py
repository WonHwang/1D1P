# 1D1P Day238 BOJ 4779번 칸토어 집합 문제 - 2021.06.30

result = []

def cantor(start, size):
    if size == 1:
        return
    cantor(start, size // 3)
    for i in range(start + (size // 3), start + (2*(size // 3))):
        result[i] = ' '
    
    cantor(start + 2*(size // 3), size // 3)
    

while True:
    try:
        N = int(input())
        result = ['-'] * (3**N)
        cantor(0, 3**N)
        print(''.join(result))

    except:
        break