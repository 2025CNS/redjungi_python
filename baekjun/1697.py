n,k = map(int,input().split())

from collections import deque
def bfs(start, target):
  visited = [False]*100001
  queue = deque()
  queue.append((start,0))
  visited[start] = True
  
  while queue:
    mov, time = queue.popleft()
    if mov == target:
      return time
    for next in (mov-1,mov+1,mov*2):
      if 0 <= next < 100001 and not visited[next]:
        visited[next] = True
        queue.append((next, time+1))
print(bfs(n,k))
  
  