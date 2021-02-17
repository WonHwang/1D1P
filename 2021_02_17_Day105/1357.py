# 1D1P Day105 1357번 뒤집힌 덧셈 문제 - 2021.02.17

X, Y = input().split()
print(int(str(int(X[::-1]) + int(Y[::-1]))[::-1]))