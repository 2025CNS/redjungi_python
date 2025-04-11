import sys
input = sys.stdin.readline

t = int(input())
data = [int(input()) for _ in range(t)]
stack = []
result = []
n = 1
try:
  for i in range(t):
    for k in range(data[i]+1):
      if data[i] >= n:
        stack.append(n)
        result.append('+')
        n += 1
        continue
      elif data[i] <= n:
        if len(stack) > 0:
          if data[i] == stack[-1]:
            result.append('-')
            stack.pop()
            break
        stack.pop()
  print('\n'.join(result))
except:
  print("NO")

