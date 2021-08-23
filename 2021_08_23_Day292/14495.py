# 1D1P Day292 BOJ 14495번 피보나치 비스무리한 수열 문제 - 2021.08.23

fibo = [0] * 117
fibo[1] = 1
fibo[2] = 1
fibo[3] = 1

for i in range(4, 117):
    fibo[i] = fibo[i-1] + fibo[i-3]

n = int(input())

print(fibo[n])