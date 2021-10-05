# 1D1P Day335 BOJ 5800번 성적 통계 문제 - 2021.10.05

for tc in range(1, int(input()) + 1):

    grade = list(map(int, input().split()))[1:]
    grade.sort()
    gap = 0
    for i in range(len(grade) - 1):
        if grade[i+1] - grade[i] > gap:
            gap = grade[i+1] - grade[i]

    print(f"Class {tc}")
    print(f"Max {grade[-1]}, Min {grade[0]}, Largest gap {gap}")