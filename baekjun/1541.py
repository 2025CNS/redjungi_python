expression = input().split('-')
result = 0

first = sum(map(int,expression[0].split('+')))
result += first

for i in expression[1:]:
  result -= sum(map(int, i.split('+')))
print(result)

