# 1D1P Day46 BOJ 1927번 최소 힙 문제 - 2020.12.20

from sys import stdin

class minheap():

    def __init__(self):
        self.arr = [None]
        self.length = 0
    
    def swap(self, index_a, index_b):
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
    
    def left(self, index):
        return 2*index
    
    def right(self, index):
        return 2*index + 1
    
    def push(self, element):
        self.arr.append(element)
        index = self.length + 1
        while index > 1:
            if self.arr[index] < self.arr[index // 2]:
                self.swap(index, index // 2)
            index = index // 2
        self.length += 1
    
    def minHeapify(self, index):
        left_index = self.left(index)
        right_index = self.right(index)
        min_index = index

        if left_index <= self.length:
            if self.arr[left_index] < self.arr[min_index]:
                min_index = left_index
        
        if right_index <= self.length:
            if self.arr[right_index] < self.arr[min_index]:
                min_index = right_index
        
        if min_index != index:
            self.swap(index, min_index)
            self.minHeapify(min_index)
    
    def pop(self):
        if self.length > 0:
            result = self.arr[1]
            self.arr[1] = self.arr[self.length]
            del(self.arr[self.length])
            self.length -= 1
            self.minHeapify(1)
            return result
        else:
            return 0
    def printf(self):
        print(self.arr[1:])

N = int(stdin.readline().rstrip())

heap = minheap()

for _ in range(N):
    x = int(stdin.readline().rstrip())
    if x == 0:
        print(heap.pop())
    else:
        heap.push(x)