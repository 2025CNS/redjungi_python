import sys
input = sys.stdin.readline

n = int(input())

class MaxHeap():
  def __init__(self):
    self.heap = [None]

  def push(self,num):
    self.heap.append(num)
    idx = len(self.heap)-1
    while idx > 1:
      parent = idx // 2
      if self.heap[parent] < self.heap[idx]:
        self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
        idx = parent
      else:
        break
  
  def pop(self):
    if len(self.heap) <= 1:
      return 0
    if len(self.heap) == 2:
      return self.heap.pop()
    
    max = self.heap[1]
    self.heap[1] = self.heap.pop()
    idx = 1
    
    
    while True:
      left = idx * 2
      right = idx * 2 + 1
      largest = idx

      if left < len(self.heap) and self.heap[left] > self.heap[largest]:
        largest = left
      if right < len(self.heap) and self.heap[right] > self.heap[largest]:
        largest = right

      if largest != idx:
        self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
        idx = largest
      else:
        break
    
    return max

max_haep=MaxHeap()
result=[]
for i in range(n):
  num = int(input())
  if num == 0:
    result.append(max_haep.pop())
  else:
    max_haep.push(num)
print("\n".join(map(str,result)))
