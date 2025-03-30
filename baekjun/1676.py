n = int(input())
result = 0
def f(num):
  num = 1
  for i in range(2,n+1):
    num *= i
  return num
result = f(n)
count = 0
for i in range(len(str(result))-1,0,-1):
  if str(result)[i] == "0":
    count += 1
    continue
  else:
    break
print(count)

  