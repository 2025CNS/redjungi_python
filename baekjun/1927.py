import sys
input = sys.stdin.readline
t = int(input())
class Minheap():
  def __init__(self):
    self.heap = []
    
  def heapify_up(self):
    idx = len(self.heap) - 1
    while idx>0:
      parent = (idx - 1) // 2
      if self.heap[parent] > self.heap[idx]:
          self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
          idx = parent
      else:
          break

  def append(self,num):
    self.heap.append(num)
    self.heapify_up()

  def pop(self):
    if not self.heap:
      return 0
    if len(self.heap) == 1:
      return self.heap.pop()
    min = self.heap[0]
    self.heap[0] = self.heap.pop()
    self.heapify_down()
    return min
  
  def heapify_down(self):
    idx = 0
    length = len(self.heap)
    while True:
      left = 2*idx+1
      right = 2*idx+2
      min = idx
      if left < length and self.heap[left] < self.heap[idx]:
        min = left
      if right < length and self.heap[right] < self.heap[min]:
        min = right
      if min == idx:
        break
      self.heap[min],self.heap[idx] = self.heap[idx],self.heap[min]
      idx = min
      

result = []
heap = Minheap()
for i in range(t):
  n = int(input())
  if n == 0:
    result.append(heap.pop())
  else:
    heap.append(n)
print("\n".join(map(str,result)))
