# 1D1P Day47 BOJ 11286번 절대값 큐 문제 - 2020.12.21

from sys import stdin

class absminheap():

    def __init__(self):
        self.arr = [None]
        self.length = 0
    
    def swap(self, index_a, index_b):
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
    
    def left(self, index):
        return 2 * index
    
    def right(self, index):
        return 2 * index + 1
    
    def absminHeapify(self, index):
        left_index = self.left(index)
        right_index = self.right(index)
        minimum_index = index

        if left_index <= self.length:
            if self.compare(left_index, minimum_index):
                minimum_index = left_index
        
        if right_index <= self.length:
            if self.compare(right_index, minimum_index):
                minimum_index = right_index
        
        if minimum_index != index:
            self.swap(index, minimum_index)
            self.absminHeapify(minimum_index)
    
    def compare(self, index_a, index_b):
        if abs(self.arr[index_a]) < abs(self.arr[index_b]):
            return 1
        elif abs(self.arr[index_a]) == abs(self.arr[index_b]) and self.arr[index_a] < self.arr[index_b]:
            return 1
        else:
            return 0
    
    def push(self, element):
        self.arr.append(element)
        self.length += 1
        index = self.length

        while index > 1:
            if self.compare(index, index // 2):
                self.swap(index, index // 2)
            index = index // 2
    
    def pop(self):
        if self.length > 0:
            result = self.arr[1]
            self.arr[1] = self.arr[self.length]
            del(self.arr[self.length])
            self.length -= 1
            self.absminHeapify(1)
            return result
        else:
            return 0

    def printf(self):
        print(self.arr[1:])


N = int(stdin.readline().rstrip())

heap = absminheap()

for _ in range(N):
    x = int(stdin.readline().rstrip())
    if x == 0:
        print(heap.pop())
    else:
        heap.push(x)