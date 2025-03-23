t = int(input())
n = list(map(int,input().split()))
count = 0
check = 0
for i in range(len(n)):
  check = 0
  for k in range(1,n[i]+1):
    if n[i]%k==0:
      check += 1
  if check == 2:
    count += 1
print(count)