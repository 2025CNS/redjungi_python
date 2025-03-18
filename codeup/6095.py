n = int(input())
li = []

for i in range(19):
  li.append([])
  for k in range(19):
    li[i].append(0)

for i in range(n):
  x,y = map(int, input().split())
  li[x-1][y-1] = 1
  
for i in range(19):
  for j in range(19):
    print(li[i][j],end=' ')
  print()