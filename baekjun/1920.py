import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
a.sort()
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))

def binary_search(arr, target, start, end):
  if start > end:
    return 0
  min = (start+end)//2
  if arr[min] == target:
    return 1
  elif arr[min] > target:
    return binary_search(arr,target,start,min-1)
  else:
    return binary_search(arr,target,min+1,end)

for i in range(m):
  print(binary_search(a,b[i],0,n-1))
  