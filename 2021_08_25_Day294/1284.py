# 1D1P Day294 BOJ 1284번 집 주소 문제 - 2021.08.25

while True:
    string = input()
    if string == '0':
        break

    answer = 1
    for digit in string:
        if digit == '0':
            answer += 4
        
        elif digit == '1':
            answer += 2
        
        else:
            answer += 3
        
        answer += 1
    
    print(answer)