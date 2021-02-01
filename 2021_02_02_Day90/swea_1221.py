# 1D1P Day90 SWEA 1221번 GNS 문제 - 2021.02.02

for t in range(1, int(input()) + 1):
    _, N = input().split()
    numbers = input().split()
    number = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    number_dict = dict()

    for num in numbers:
        number_dict[num] = number_dict.get(num, 0) + 1
    
    print(_)
    for num in number:
        for i in range(number_dict[num]):
            print(num, end=" ")