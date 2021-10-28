# 1D1P Day358 BOJ 2052번 꼬리를 무는 숫자 나열 문제 - 2021.10.28

def grid(N):
    return (N-1) // 4, (N-1) % 4

a, b = map(int, input().split())
ax, ay = grid(a)
bx, by = grid(b)
print(abs(ax - bx) + abs(ay - by))