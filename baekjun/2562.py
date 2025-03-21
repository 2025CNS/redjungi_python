max = 0
count = 0
for i in range(9):
  n = int(input())
  if max<n:
    max = n
    count = i+1
print(max)
print(count)