m = []
ant_x = 2
ant_y = 2
for i in range(10): #m리스트 초기화
  m.append([])
  for j in range(10):
    m[i].append(0)

for i in range(10):
  temp = input().split()
  for j in range(10):  
    m[i][j]=int(temp[j])

m[ant_y-1][ant_x-1] = 9

while 1: #개미
  m[ant_y-1][ant_x-1] = 9
  if (m[ant_y-1][ant_x] == 0):
    ant_x = ant_x+1
  elif m[ant_y-1][ant_x] == 1 and m[ant_y][ant_x-1]==0:
    ant_y = ant_y+1
  elif m[ant_y-1][ant_x] == 2 or m[ant_y][ant_x-1] == 2:
    if m[ant_y-1][ant_x] == 2:
      m[ant_y-1][ant_x] = 9
      break
    else:
      m[ant_y][ant_x-1] = 9
      break
  else:
    m[ant_y-1][ant_x-1] = 9
    break


for i in range(10): #출력
  for j in range(10):
    print(m[i][j],end=' ')
  print()