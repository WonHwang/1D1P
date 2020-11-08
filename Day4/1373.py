# 1D1P Day4 BOJ 1373번 2진수 8진수 문제 - 2020.11.08

base = {'000' : '0', '001' : '1', '010' : '2', '011' : '3', '100' : '4', '101' : '5', '110' : '6', '111' : '7'}

N = input()
answer = ''

if len(N) % 3 == 1:
    N = '00' + N
elif len(N) % 3 == 2:
    N = '0' + N

for i in range(int(len(N)/3)):
    tmp = N[3*i : 3*i + 3]
    answer += base[tmp]

print(answer)