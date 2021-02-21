# 1D1P Day109 BOJ 1076번 저항 문제 - 2021.02.21

table = {'black' : 0,
'brown' : 1,
'red' : 2,
'orange' : 3,
'yellow' : 4,
'green' : 5,
'blue' : 6,
'violet' : 7,
'grey' : 8,
'white' : 9}

color1 = input()
color2 = input()
multiple = input()

result = int(str(table[color1]) + str(table[color2])) * (10 ** table[multiple])
print(result)