# 1D1P Day265 BOJ 2864번 5와 6의 차이 문제 - 2021.07.27

A_set = set()
B_set = set()

def makeset(string, element, depth, Type):

    if depth == len(string):
        if Type == 'A':
            A_set.add(element)
        else:
            B_set.add(element)
        return
    
    if string[depth] == '5' or string[depth] == '6':
        makeset(string, element+'5', depth+1, Type)
        makeset(string, element+'6', depth+1, Type)
    
    else:
        makeset(string, element+string[depth], depth+1, Type)


A, B = map(str, input().split())
makeset(A, '', 0, 'A')
makeset(B, '', 0, 'B')


Min, Max = 3000000, 0

for a in A_set:
    for b in B_set:
        a, b = int(a), int(b)
        if a + b > Max:
            Max = a+b
        if a + b < Min:
            Min = a+b

print(Min, Max)