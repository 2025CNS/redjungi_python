import sys
input = sys.stdin.readline

class AbsHeap:
  def __init__(self):
    self.heap = [0]
  
  def push(self, value):
    self.heap.append(value)
    idx = len(self.heap)-1
    
    while idx > 1:
      parent = idx//2
      if self.compare(self.heap[idx],self.heap[parent]):
        self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
        idx = parent
      else:
        break
  
  def compare(self, a, b):
    if abs(a) < abs(b):
      return True
    elif abs(a) == abs(b):
      return a<b
    else:
      return False
    
  def pop(self):
    if len(self.heap) == 1:
      return 0
    
    top = self.heap[1]
    self.heap[1] = self.heap[-1]
    self.heap.pop()
    self.heapify(1)
    return top
  
  def heapify(self, i):
    left = i * 2
    right = i * 2 + 1
    smallest = i
    if left < len(self.heap) and self.compare(self.heap[left], self.heap[smallest]):
      smallest = left
    if right < len(self.heap) and self.compare(self.heap[right], self.heap[smallest]):
      smallest = right
    if smallest != i:
      self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
      self.heapify(smallest)
    

t = int(input())
abs_heap = AbsHeap()
result = []
for i in range(t):
  n = int(input())
  if n == 0:
    result.append(abs_heap.pop())
  else:
    abs_heap.push(n)
    
print("\n".join(map(str,result)))
