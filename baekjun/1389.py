n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
def bfs(start,graph,target):
  cnt = 0
  visited = [False]*(n+1)
  queue = deque([start])
  visited[start] = True
  
  while queue:
    for _ in range(len(queue)):
      node = queue.popleft()
      if node == target:
        return cnt
      for neighbor in graph[node]:
        if not visited[neighbor]:
          queue.append(neighbor)
          visited[neighbor] = True
    cnt += 1

result = []
for i in range(1,n+1):
  total = 0
  for j in range(1,n+1):
    total += bfs(i,graph,j)
  result.append(total)

print(result.index(min(result))+1)
