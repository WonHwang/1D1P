# 1D1P Day317 BOJ 15904�� UCPC�� ������ �����ϱ�? ���� - 2021.09.17

words = input()
target = "UCPC"
answer = 0
idx = 0

for word in words:
    if word == target[idx]:
        idx += 1

    if idx == 4:
        answer = 1
        break

result = 'love' if answer else 'hate'
print(f"I {result} UCPC")