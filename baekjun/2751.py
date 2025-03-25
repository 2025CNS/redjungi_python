import sys
import random
t = int(sys.stdin.readline())
n = [[0]] * t
for r in range(t):
    n[r] = int(sys.stdin.readline().strip())

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


sys.stdout.write("\n".join(map(str, quick_sort(n))) + "\n")