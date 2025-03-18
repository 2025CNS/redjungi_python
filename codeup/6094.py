a = int(input())
num = input().split()
result = []
for i in range(a): #num 형변환
  num[i] = int(num[i])

mini = 100
for i in range(0,a):
  if mini>num[i]:
    mini = num[i]

print(mini)
