r,g,b= map(int,input().split())

i = 0
k = 0
j = 0
count =0
while(i<r):
  k=0
  while(k<g):
    j=0
    while(j<b):
      print("%d %d %d" %(i,k,j))
      count = count+1
      j = j+1
    k = k+1
  i = i+1
print(count)
