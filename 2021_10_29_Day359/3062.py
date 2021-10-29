# 1D1P Day359 BOJ 3062번 수 뒤집기 문제 - 2021.10.29

for _ in range(int(input())):
    num = input()
    tmp = str(int(num) + int(num[::-1]))
    if tmp == tmp[::-1]:
        print("YES")
    else:
        print("NO")