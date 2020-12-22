# 1D1P Day48 BOJ 1655번 가운데를 말해요 문제 - 2020.12.22

from sys import stdin
import heapq

def main():
    N = int(stdin.readline().rstrip())
    mid = int(stdin.readline().rstrip())
    max_heap = []
    min_heap = []
    print(mid)
    for i in range(2, N+1):
        x = int(stdin.readline().rstrip())
        if x >= mid:
            heapq.heappush(min_heap, x)
            if len(min_heap) > len(max_heap) + 1:
                heapq.heappush(max_heap, -mid)
                mid = heapq.heappop(min_heap)
        else:
            heapq.heappush(max_heap, -x)
            if len(max_heap) > len(min_heap):
                heapq.heappush(min_heap, mid)
                mid = -heapq.heappop(max_heap)
        print(mid)

main()