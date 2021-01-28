a, b = input().split()
a_ = a.split('.')
under_point = len(a_[1])
if a_[0] != '0':
    a = int(a_[0] + a_[1])
    a **= int(b)
    a = str(a)
    under_point *= int(b)
    over = a[:-under_point]
    under = a[-under_point:]
    result = over + '.' + under
    print(result)
else:
    under_point *= int(b)
    a = int(a_[1]) ** int(b)
    result = '0.' + str(a).zfill(under_point)
    print(result)