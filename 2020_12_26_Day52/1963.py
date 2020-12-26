# 1D1P Day52 BOJ 1963번 소수 경로 문제 - 2020.12.26

from sys import stdin
from collections import deque

def isprime(n):

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return True


primes = {}

for i in range(1000, 10000):
    if isprime(i):
        primes[str(i)] = 1

N = int(stdin.readline().rstrip())

for _ in range(N):
    start, end = map(str, stdin.readline().rstrip().split(' '))

    visited = dict()
    for key in primes:
        visited[key] = 0
    
    queue = deque()
    queue.append([start, 0])
    visited[start] = 1
    while queue:
        node = queue.popleft()
        num, step = node[0], node[1]
        if num == end:
            print(step)
            break
        for digit in range(10):
            if digit == 0:
                first = num
                second = num[0] + str(digit) + num[2:]
                third = num[:2] + str(digit) + num[-1]
                fourth = num[:3] + str(digit)
            else:
                first = str(digit) + num[1:]
                second = num[0] + str(digit) + num[2:]
                third = num[:2] + str(digit) + num[-1]
                fourth = num[:3] + str(digit)
            
            if first in primes:
                if visited[first] == 0:
                    queue.append([first, step + 1])
                    visited[first] = 1
            
            if second in primes:
                if visited[second] == 0:
                    queue.append([second, step + 1])
                    visited[second] = 1
            
            if third in primes:
                if visited[third] == 0:
                    queue.append([third, step + 1])
                    visited[third] = 1
            
            if fourth in primes:
                if visited[fourth] == 0:
                    queue.append([fourth, step + 1])
                    visited[fourth] = 1
    
    if num != end:
        print("Impossible")