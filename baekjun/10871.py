n, x = map(int,input().split())
l = input().split()

for i in range(n):
  if int(l[i]) < x:
    print(l[i],end=' ')
    