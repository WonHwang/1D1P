# 1D1P Day150 BOJ 2290번 LCD Test 문제 - 2021.04.03

s, n = map(str, input().split())
s = int(s)

answer = ['' for _ in range(2*s + 3)]

def col2(s):
    
    for i in range(2*s + 3):
        if i == 0 or i == 2*s + 2 or i == s + 1:
            answer[i] += ' '
        else:
            answer[i] += '|'

def colup(s):
    for i in range(2*s + 3):
        if i == 0 or i > s:
            answer[i] += ' '
        else:
            answer[i] += '|'

def coldown(s):
    for i in range(2*s + 3):
        if s+1 < i < 2*s + 2:
            answer[i] += '|'
        else:
            answer[i] += ' '

def row3(s):
    for i in range(2*s + 3):
        if i == 0 or i == 2*s + 2 or i == s+1:
            answer[i] += '-'
        else:
            answer[i] += ' '

def rowup(s):
    for i in range(2*s + 3):
        if i == 0:
            answer[i] += '-'
        else:
            answer[i] += ' '

def rowmid(s):
    for i in range(2*s + 3):
        if i == s+1:
            answer[i] += '-'
        else:
            answer[i] += ' '

def rowupbot(s):
    for i in range(2*s + 3):
        if i == 0 or i == 2*s + 2:
            answer[i] += '-'
        else:
            answer[i] += ' '

def blank(s):
    for i in range(2*s + 3):
        answer[i] += ' '

def draw(s, digit):

    if digit == '1':
        for i in range(s+2):
            if i == s+1:
                col2(s)
            else:
                blank(s)
    
    elif digit == '2':
        for i in range(s+2):
            if i == 0:
                coldown(s)
            elif i == s+1:
                colup(s)
            else:
                row3(s)
    
    elif digit == '3':
        for i in range(s+2):
            if i == 0:
                blank(s)
            elif i == s+1:
                col2(s)
            else:
                row3(s)
    
    elif digit == '4':
        for i in range(s+2):
            if i == 0:
                colup(s)
            elif i == s+1:
                col2(s)
            else:
                rowmid(s)
    
    elif digit == '5':
        for i in range(s+2):
            if i == 0:
                colup(s)
            elif i == s+1:
                coldown(s)
            else:
                row3(s)
        
    elif digit == '6':
        for i in range(s+2):
            if i == 0:
                col2(s)
            elif i == s+1:
                coldown(s)
            else:
                row3(s)
    
    elif digit == '7':
        for i in range(s+2):
            if i == 0:
                blank(s)
            elif i == s+1:
                col2(s)
            else:
                rowup(s)
    
    elif digit == '8':
        for i in range(s+2):
            if i == 0 or i == s+1:
                col2(s)
            else:
                row3(s)
    
    elif digit == '9':
        for i in range(s+2):
            if i == 0:
                colup(s)
            elif i == s+1:
                col2(s)
            else:
                row3(s)
    
    elif digit == '0':
        for i in range(s+2):
            if i == 0 or i == s+1:
                col2(s)
            else:
                rowupbot(s)
    
    blank(s)

for digit in n:
    draw(s, digit)

for i in range(2*s + 3):
    print(answer[i])