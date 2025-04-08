import sys

t = int(sys.stdin.readline())

queue = [0]*t
result = []
frist = 0
next = 0

for _ in range(t):
  cmnd = input()
  if "push" in cmnd:
    queue[next] = int(cmnd[5:])
    next += 1
  elif "pop" in cmnd:
    if queue[frist] == 0:
      result.append(-1)
    else:
      result.append(queue[frist])
      queue[frist] = 0
      frist += 1
  elif "size" in cmnd:
    result.append(next-frist)
  elif "empty" in cmnd:
    count = 0
    for i in range(next-frist):
      if queue[frist+i] == 0:
        count += 1
    if count == next-frist:
      result.append(1)
    else:
      result.append(0)
  elif "front" in cmnd:
    if queue[frist] == 0:
      result.append(-1)
    else:
      result.append(queue[frist])
  elif "back" in cmnd:
    if queue[next-1] == 0:
      result.append(-1)
    else:
      result.append(queue[next-1])
    
for i in result:
  print(i)