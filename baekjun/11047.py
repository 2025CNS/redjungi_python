import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coin = []
for i in range(n):
  coin.append(int(input()))
count = 0

for i in range(n):
  if k == 0:
    break
  if coin[n-1-i] <= k:
    count += k//coin[n-1-i]
    k = k%coin[n-1-i]
print(count)