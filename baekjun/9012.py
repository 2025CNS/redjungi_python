t = int(input())
s = []
result = []
for i in range(t):
  s.append(input())
stack = []
for i in range(len(s)):
  stack.clear()
  for k in s[i]:
    if k == '(':
      stack.append(k)
    elif k == ')':
      if len(stack) != 0:
        if stack[-1] == '(':
          stack.pop()
      else:
        stack.append(k)
  if len(stack) == 0:
    result.append("YES")
  else:
    result.append("NO")

for i in range(len(result)):
  print(result[i])