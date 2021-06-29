# 1D1P Day237 BOJ 7789번 텔레프라임 문제 - 2021.06.29

def checkprime(N):

    if not N%2 and N > 2:
        return False

    for i in range(3, int(N**0.5) + 1, 2):
        if not N%i:
            return False
    return True
a, b = map(int, input().split())
print('Yes' if checkprime(a) and checkprime((10**6)*b + a) else 'No')