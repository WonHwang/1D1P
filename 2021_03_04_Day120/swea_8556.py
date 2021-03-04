# 1D1P Day120 SWEA 8556번 북북서 문제 - 2021.03.04

def gcd(a, b):
    if b > a:
        a, b = b, a
    
    while b > 0:
        a, b = b, a % b
    
    return a


for tc in range(1, int(input()) + 1):

    n = 0
    string = list(input())
    string = string[::-1] + [0]
    arr = []
    while string:
        if string[0] == 't':
            arr.append('w')
            string = string[4:]
            n += 1
        elif string[0] == 'h':
            arr.append('n')
            string = string[5:]
            n += 1
        else:
            break
    
    base = 2 ** (n - 1)
    top = 0
    if arr[0] == 'w':
        top += 90 * base
    for i in range(1, len(arr)):
        if arr[i] == 'w':
            top += 90 * (2 ** (n-1-i))
        elif arr[i] == 'n':
            top -= 90 * (2 ** (n-1-i))
    
    gcd_ = gcd(top, base)
    if gcd_ == base:
        answer = top // base
    else:
        top //= gcd_
        base //= gcd_
        answer = str(top) + '/' + str(base)
    
    print(f"#{tc} {answer}")