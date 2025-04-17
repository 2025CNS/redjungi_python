import sys
input = sys.stdin.readline

n,m = map(int,input().split())
hearX = {}
hearSeeX = []
for i in range(n):
  name = input().strip()
  hearX[name] = False
for i in range(m):
  name = input().strip()
  try:
    hearX[name] += True
  except:
    continue
hearSeeX = [key for key, value in hearX.items() if value == True]
hearSeeX.sort()
a = len(hearSeeX)
print(a)
for i in range(a):
  print(hearSeeX[i])