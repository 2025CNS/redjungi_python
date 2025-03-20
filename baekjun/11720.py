n = int(input())
total = 0
a = []
a.append(list(map(int,input())))
for i in range(n):
  total += a[0][i]
print(total)