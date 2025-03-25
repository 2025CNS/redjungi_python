t = int(input())
prs = []
result=[]
for i in range(t):
  k = int(input())#0,1=1 0,2=2 0,3=3
  n = int(input())#1,1=1 1,2=3 1,3=6
  for j in range(1,n+1):#0층 사람수
    prs.append(j)
  for j in range(1,n+1):
    prs[j-1]=j
  if k == 0:
    print(prs[n-1])
    continue
  for j in range(k):#2,1=1 2,2=4 2,3 = 10
    a=0
    for o in range(n):
      temp=0
      for l in range(n-a):#3,1=1 3,2=5 3,3 = 15
        temp += prs[l]#4,1=1 4,2=6 4,3=21
      prs[n-a-1]=temp
      a += 1          #5,1=1 5,2=7 5,3=28
  result.append(prs[n-1])

for i in range(len(result)):
  print(result[i])