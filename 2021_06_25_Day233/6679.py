# 1D1P Day233 BOJ 6679번 싱기한 네자리 숫자 문제 - 2021.06.25
# 순국선열에 대한 묵념

notation = '0123456789abcdef'

def change(number, base):
    q, r = divmod(number, base)
    n = notation[r]
    return change(q, base) + n if q else n

for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                num = i*1000 + j*100 + k*10 + l
                dec = i + j + k + l
                twelve = change(num, 12)
                sixteen = change(num, 16)
                twv = 0
                for digit in twelve:
                    twv += int(digit, 12)
                sxt = 0
                for digit in sixteen:
                    sxt += int(digit, 16)
                
                if dec == twv == sxt:
                    print(num)