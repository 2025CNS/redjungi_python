n, m = map(int,input().split())
user = 0
result = []
cn = list(map(int,input().split()))

for i in range(n):
  for k in range(i+1,n):
    for j in range(k+1,n):
      user = cn[i]+cn[k]+cn[j]
      if user > m:
        continue
      else:
        result.append(user)
result.sort()
print(result[-1])