import sys
input = sys.stdin.readline
total = 0
gg = 0
for i in range(20):
  s,f,g = map(str,input().split())
  if g=='P':
    continue
  total += float(f)
  if g == 'A+':
    gg += float(f)*4.5
  elif g=='A0':
    gg += float(f)*4.0
  elif g=='B+':
    gg += float(f)*3.5
  elif g=='B0':
    gg += float(f)*3.0
  elif g=='C+':
    gg += float(f)*2.5
  elif g=='C0':
    gg += float(f)*2.0
  elif g=='D+':
    gg += float(f)*1.5
  elif g=='D0':
    gg += float(f)*1.0
  elif g=='F':
    gg += float(f)*0.0
print(gg/total)