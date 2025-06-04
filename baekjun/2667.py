import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
def dfs(x,y):
  global count
  global arr
  visited[x][y] = True
  arr[x][y] = 2
  count += 1
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    
    if 0 <= nx < n and 0 <= ny < n:
      if arr[nx][ny]==1 and not visited[nx][ny]:
        dfs(nx,ny)

#입력
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int,input().strip())))

visited = [[False]*n for _ in range(n)]
result = []
for i in range(n):
  for j in range(n):
    if arr[i][j]==1:
      dfs(i,j)
      result.append(count)
      count = 0
result = sorted(result)
print(len(result),"\n".join(map(str,result)),sep='\n')


