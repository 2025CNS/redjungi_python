a = int(input())
num = input().split()
result = []
for i in range(a): #num 형변환
  num[i] = int(num[i])

i = a-1
while(i>=0):
  print(num[i],end=' ')
  i-=1
