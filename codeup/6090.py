a, b, d, c = map(int,input().split())
total = a
for i in range(1, c ,1):
  total = total*b+d
print(total)
