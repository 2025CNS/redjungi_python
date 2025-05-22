p = list(map(int,input().split()))
x,y,r = map(int,input().split())
check = False
for i in p:
  if i==x:
    print(p.index(i)+1)
    check = True
if check==False:
  print(0)

