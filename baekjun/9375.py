t = int(input())
result = []
for i in range(t):
  n = int(input())
  category = {}

  for j in range(n):
    name, cate = input().split()
    if cate in category:
        category[cate] += 1
    else:
        category[cate] = 1
  answer = 1
  for count in category.values():
      answer *= (count + 1)
  result.append(answer-1)
print("\n".join(map(str,result)))
