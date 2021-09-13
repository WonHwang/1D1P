# 1D1P Day313 BOJ 11068번 회문인 수 문제 - 2021.09.13

digit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def numtobasen(num, n):

    result = ''

    while num > 0:
        result += digit[num%n]
        num //= n
    
    return result[::-1]

for _ in range(int(input())):
    
    number = int(input())
    answer = 0

    for i in range(2, 65):
        if i == 10:
            number_ = str(number)
        else:
            number_ = numtobasen(number, i)
        if number_ == number_[::-1]:
            answer = 1
            break
    
    print(answer)