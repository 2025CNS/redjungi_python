h, w = map(int,input().split())
n = int(input())
border = []

for i in range(h):
  border.append([])
  for k in range(w):
    border[i].append(0)

for j in range(n):
  i,d,x,y = map(int,input().split())
  if(d == 1):
    for u in range(i):
      border[x+u-1][y-1] = 1
  else:
    for u in range(i):
      border[x-1][y+u-1] = 1
            #y    x


for i in range(h):
  for k in range(w):
    print(border[i][k],end=' ')
  print()
