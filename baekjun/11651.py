import sys

t = int(sys.stdin.readline())
n = []
for i in range(t):
  n.append(list(map(int,sys.stdin.readline().split())))

n.sort(key=lambda x : (x[1],x[0]))
#print("------------------------")
for i in range(t):
  for k in range(2):
    print(n[i][k],end=' ')
  print()