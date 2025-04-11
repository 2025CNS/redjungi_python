import sys
import random
input = sys.stdin.readline

def quick_sort(arr):
  if len(arr)<=1:
    return arr
  
  qivot = arr[random.randrange(0,len(arr))]
  s,m,l = [],[],[]
  for i in range(len(arr)):
    if arr[i] < qivot:
      s.append(arr[i])
    elif arr[i] > qivot:
      l.append(arr[i])
    else:
      m.append(arr[i])
  return quick_sort(s)+m+quick_sort(l)

t = int(input())
data = [int(input()) for _ in range(t)]

total = sum(data)
print(round(total/t))
data = quick_sort(data)
print(data[t//2])
#최빈값
cnt = 0
result = [0]*8001
for i in data:
  result[i+4000] += 1
indices = [i for i, v in enumerate(result) if v == max(result)]
if len(indices) > 1:
  indices[1] -= 4000
  print(indices[1])
else:
  indices[0] -= 4000
  print(indices[0])
print(data[-1]-data[0])


