import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
  if x < 0 or y < 0 or x >= row or y >= col:
    return
  if arr[x][y] == 0:
    return
  
  arr[x][y] = 0

  dfs(x+1, y)  # 오른쪽
  dfs(x-1, y)  # 왼쪽
  dfs(x, y+1)  # 아래
  dfs(x, y-1) 

t = int(input())
result = []
for k in range(t):
  row,col,n = map(int,input().split())
  if n == 0:
        result.append(0)
        continue
  arr = []
  arr = [[0] * col for _ in range(row)]
  
  for i in range(n):
    x,y = map(int,input().split())
    arr[x][y] = 1
  
  count = 0
  
  for i in range(row):
    for j in range(col):
      if arr[i][j] == 1:
        dfs(i,j)
        count += 1
  result.append(count)
print("\n".join(map(str,result)))