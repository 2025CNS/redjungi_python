n = int(input())
count = 0
i = 665
while 1:
  i += 1
  if "666" in str(i):
    count += 1
    if count == n:
      break
print(i)