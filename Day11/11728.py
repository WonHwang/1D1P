# 1D1P Day11 BOJ 11728번 배열 합치기 문제 - 2020.11.15

A, B = map(int, input().split(' '))

array_A = input().split(' ')
array_B = input().split(' ')

for i in range(A):
    array_A[i] = int(array_A[i])
for i in range(B):
    array_B[i] = int(array_B[i])

new_array = array_A + array_B

new_array.sort()

answer = ''

for i in range(A+B):
    answer += str(new_array[i]) + ' '

answer = answer[:-1]
print(answer)