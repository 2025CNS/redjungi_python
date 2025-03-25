a,b,v = map(int,input().split())
d = 0
total = 0
if a>=v:
  d = 1
else:
  if(v-a)%(a-b) == 0:
    d = (v-a)//(a-b)+1
  elif (v-a)%(a-b) != 0:
    d = (v-a)//(a-b)+2

print(d)