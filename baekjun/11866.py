# 1 0 0 4 5 0 7
#       f      

n,k = map(int,input().split())

queue = list(range(1,n+1))
frist = 0
result = []
while 1:
  if len(result) == n:
    break
  if queue[frist] == 0:
    frist += 1
    if frist >= len(queue):
      frist=0
    continue
  else:
    for i in range(k-1):
      frist += 1
      if frist >= len(queue):
        frist = 0
      while 1:
        if frist >= len(queue):
          frist = 0
        elif queue[frist] == 0:
          frist += 1
        else:
          break
    if frist > len(queue)-1:
      frist = frist-len(queue)
    result.append(queue[frist])
    queue[frist] = 0

print('<' + ', '.join(map(str, result)) + '>')
  