# 1D1P Day7 BOJ 1212번 8진수 2진수 문제 - 2020.11.11

def eighttotwo(number):
    number = int(number)
    answer = ''
    while number != 0:
        answer = str(number % 2) + answer
        number = int(number / 2)
    
    while len(answer) < 3:
        answer = '0' + answer
    
    return answer

def main():
    number = input()
    if number == '0':
        return '0'
    answer = ''

    for i in range(len(number)):
        answer += eighttotwo(number[i])

    while answer[0] == '0':
        answer = answer[1:]
    
    return answer

print(main())