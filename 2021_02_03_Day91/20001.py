# 1D1P Day91 BOJ 20001번 고무오리 디버깅 문제 - 2021.02.03

stack = []
_ = input()

while True:
    s = input()
    if s == "고무오리 디버깅 끝":
        break
    elif s == '고무오리':
        if stack:
            stack.pop()
        else:
            stack.append(1)
            stack.append(1)
    else:
        stack.append(1)

if stack:
    print("힝구")
else:
    print("고무오리야 사랑해")