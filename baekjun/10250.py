t = int(input())
house = []
for i in range(t):
  h, w, n = map(int,input().split())
  floor = n%h
  room = n//h+1
  if n%h ==0:
    floor = h
    room -= 1
  house.append(str(floor) + str(room).zfill(2))

for i in range(t):
  print(house[i])
