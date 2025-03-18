a = int(input())
num = input().split()
result = []
for i in range(a): #num 형변환
  num[i] = int(num[i])

for i in range(23): #result 초기화
  result.append(0)

for i in range(a): #result 값넣기
  result[num[i]-1]+= 1

for i in range(23):
  print(result[i],end=' ')
