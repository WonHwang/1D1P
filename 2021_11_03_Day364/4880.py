# 1D1P Day364 BOJ 4880번 다음수 문제 - 2021.11.03

while True:
    a, b, c = map(int, input().split())
    if not a and not b and not c:
        break

    if b**2 == a*c:
        print(f"GP {c*(b//a)}")
        pass

    elif 2*b == a+c:
        print(f"AP {c+(b-a)}")