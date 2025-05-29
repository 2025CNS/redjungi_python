import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n, m = map(int, input().split())
campus = []
for _ in range(n):
  campus.append(list(input().strip()))

cnt = 0

def dfs(x, y):
  global cnt
  if x < 0 or x >= n or y < 0 or y >= m:
    return
  if campus[x][y] == 'X' or campus[x][y] == 'V':
    return
  if campus[x][y] == 'P':
    cnt += 1
  campus[x][y] = 'V'

  dfs(x+1, y)
  dfs(x-1, y)
  dfs(x, y+1)
  dfs(x, y-1)

for i in range(n):
  for j in range(m):
    if campus[i][j] == 'I':
      dfs(i, j)

if cnt == 0:
  print("TT")
else:
  print(cnt)