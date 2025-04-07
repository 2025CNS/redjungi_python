import sys

t = int(sys.stdin.readline().strip())
N_s = list(map(int, sys.stdin.readline().strip().split()))
t2 = int(sys.stdin.readline().strip())
M_s = list(map(int, sys.stdin.readline().strip().split()))
n_dic = {}

def Quick_Sort(n):
  if len(n) <= 1:
    return n
  pivot = n[len(n)//2]
  sl,ml,ll = [],[],[]
  for i in n:
    if i < pivot:
      sl.append(i)
    elif i > pivot:
      ll.append(i)
    else:
      ml.append(i)
  return Quick_Sort(sl)+ml+Quick_Sort(ll)

def binary(m, N_s, start, end):
    if start > end:
        return 0
    mid = (start + end)//2
    if m == N_s[mid]:
        return n_dic[m]
    elif m < N_s[mid]:
        return binary(m, N_s, start, mid-1)
    else:
        return binary(m, N_s, mid+1, end)

N_s = Quick_Sort(N_s)

for n in N_s:
  if n in n_dic:
    n_dic[n] += 1
  else:
    n_dic[n] = 1

for m in M_s:
  print(binary(m, N_s, 0, len(N_s)-1), end=' ')
