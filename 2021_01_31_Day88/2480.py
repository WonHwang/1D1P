a, b, c = map(int, input().split())

if a == b and b == c and c == a:
    print(10000 + a * 1000)

elif a == b and a != c:
    print(1000 + a * 100)

elif b == c and a != b:
    print(1000 + b * 100)

elif a == c and a != b:
    print(1000 + a * 100)

else:
    maxi = a
    if b > maxi:
        maxi = b
    if c > maxi:
        maxi = c
    print(maxi * 100)