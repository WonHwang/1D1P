# 1D1P Day273 BOJ 2877번 4와 7 문제 - 2021.08.04

def countDigit(K):

    k = 1

    while 2**(k+1) - 2 < K:
        k += 1
    
    return k, K-(2 ** k - 2) - 1

K = int(input())

digit, count = countDigit(K)

binary = bin(count)[2:]
binary = binary.zfill(digit)

answer = ""

for char in binary:
    if char == '0':
        answer += '4'
    else:
        answer += '7'

print(answer)