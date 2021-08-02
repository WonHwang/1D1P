# 1D1P Day271 BOJ 4504번 배수 찾기 문제 - 2021.08.02

N = int(input())
while True:
    n = int(input())
    if not n:
        break
    print(f"{n} is ", end='')
    if n%N:
        print("NOT ", end='')
    print(f"a multiple of {N}.")