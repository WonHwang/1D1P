K = int(input())
D1, D2 = map(int, input().split())

if D1 == D2:
    print(K ** 2)

elif D1 == 3*D2:
    print(K**2 - D2**2)

elif D2 == 3*D1:
    print(K**2 - D1**2)

elif D1 > D2:
    print(round((K ** 2) - (((D1 - D2) / 2) ** 2), 6))

else:
    print(round((K ** 2) - (((D2 - D1) / 2) ** 2), 6))