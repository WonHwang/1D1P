# 1D1P Day329 BOJ 16170번 오늘의 날짜는? 문제 - 2021.09.30

import time
now = time.gmtime()
print(now.tm_year)
print(str(now.tm_mon).zfill(2))
print(str(now.tm_mday).zfill(2))