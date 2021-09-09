# 1D1P Day308 BOJ 1312번 소수 문제 - 2021.09.09

# A, B, N = map(int, input().split())
# tmp = "%.101f"%(A/B)
# tmp = tmp.split('.')[1]
# for i in range(1, 100):
#     if tmp[i] == tmp[0]:
#         tmp = tmp[:i]
#         break

# length = len(tmp)
# print(tmp[(N % length) - 1]) => 순환소수가 안생기는 경우가 있기도 한가보다 왜 안되는지는 모르겠다.

def divide(A, B):

    digit = ""
    A %= B

    for _ in range(1000001):
        A *= 10

        digit += str(A // B)
        A %= B
    
    return digit

A, B, N = map(int, input().split())
print(divide(A, B)[N-1])