import sys
input = sys.stdin.readline
t = int(input())
score = []
for _ in range(t):
  score.append(int(input()))

def custom_round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

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

if t == 0:
  print(0)
else:
  score = Quick_Sort(score)
  a = custom_round(t/(100/15))
  total = 0
  for i in range(a,t-a):
    total += score[i]
  print(custom_round(total/(t-(a*2))))


