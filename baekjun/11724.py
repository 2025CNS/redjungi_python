import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

def Dfs(graph,v):
  visited[v] = True
  for next in graph[v]:
    if not visited[next]:
      Dfs(graph,next)
  

n,m = map(int,input().split())
visited = [False]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(m):
  idx,val = map(int,input().split())
  graph[idx].append(val)
  graph[val].append(idx)
cnt = 0
for i in range(1,n+1):
  if not visited[i]:
    Dfs(graph,i)
    cnt += 1
print(cnt)