# 1D1P Day259 BOJ 2754번 학점계산 문제 - 2021.07.21

grade = input()
answer = abs(ord(grade[0]) - ord('E')) if grade[0] != 'F' else 0
if answer:
    if grade[1] == '+':
        answer += 0.3
    elif grade[1] == '-':
        answer -= 0.3
print("%0.1f"%(answer))