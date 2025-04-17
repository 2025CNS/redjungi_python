import sys
input = sys.stdin.readline

n = int(input())
p = {}

time = list(map(int,input().split()))
for i in range(n):
  p[i+1] = time[i]
p = dict(sorted(p.items(), key=lambda item: item[1]))
total = 0
tmp = list(p.values())

for i in range(n+1):
  for k in range(i):
    total += tmp[k]
print(total)
  