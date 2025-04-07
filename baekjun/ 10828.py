import sys
t = int(sys.stdin.readline())

stack = []
result = []
for _ in range(t):
  cmnd = input()
  if "push" in cmnd:
    stack.append(int(cmnd[5:]))
  elif "pop" in cmnd:
    if len(stack) == 0:
      result.append(-1)
    else:
      result.append(stack[-1])
      stack.pop()
  elif "size" in cmnd:
    result.append(len(stack))
  elif "empty" in cmnd:
    if len(stack) == 0:
      result.append(1)
    else:
      result.append(0)
  elif "top" in cmnd:
    if len(stack) == 0:
      result.append(-1)
    else:
      result.append(stack[-1])
for i in result:
  print(i)
