import sys
input = sys.stdin.readline

n,m = map(int,input().split())
poketmon = {}
poketmon_num = {}
result = []
for i in range(n):
  name = input().strip()
  poketmon[name] = i+1
  poketmon_num[i+1] = name
for i in range(m):
  question = input().strip()
  if question.isdigit():
    result.append(poketmon_num[int(question)])
  else:
    result.append(poketmon[question])
for i in range(len(result)):
  print(result[i])
