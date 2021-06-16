# 1D1P Day224 BOJ 6500번 랜덤 숫자 만들기 문제 - 2021.06.16

from sys import stdin
input = stdin.readline

while True:

    string = input().rstrip()
    if string == '0':
        break

    Set = set()

    while string not in Set:
        Set.add(string)
        string = int(string)
        string **= 2
        string = str(string)
        while len(string) < 8:
            string = '0' + string
        
        string = string[2:6]
    
    print(len(Set))