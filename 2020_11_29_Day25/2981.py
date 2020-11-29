# 1D1P Day25 BOJ 2981번 검문 문제 - 2020.11.29

import sys
import math

def gcd(a, b):
    if b > a:
        tmp = b
        b = a
        a = tmp
    
    while a%b != 0:
        tmp = a%b
        a = b
        b = tmp
    
    return b

N = int(input())
numbers = []
gaps = []
for i in range(N):
    numbers.append(int(sys.stdin.readline().rstrip()))

for i in range(N-1):
    gaps.append(abs(numbers[i] - numbers[i+1]))

if N > 2:
    gcd_ = gcd(gaps[0], gaps[1])
    for i in range(2, N-1):
        gcd_ = gcd(gaps[i], gcd_)
else:
    gcd_ = gaps[0]

answer_ = set()
for i in range(1, int(gcd_ ** 0.5) + 1):
    if gcd_ % i == 0:
        answer_.add(i)
        answer_.add(int(gcd_/i))

answer_.remove(1)
answer = []
for _ in answer_:
    answer.append(_)
answer.sort()
for _ in answer:
    print(_, end=" ")