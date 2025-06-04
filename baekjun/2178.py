import sys
from collections import deque
input = sys.stdin.readline
def bfs(x,y):
  queue = deque()
  queue.append((x,y))
  
  while queue:
    x,y = queue.popleft()
      
    for m_x,m_y in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
      if 0 <= m_x < n and 0 <= m_y < m and arr[m_x][m_y] == 1:
        arr[m_x][m_y] = arr[x][y] + 1
        queue.append((m_x,m_y))
  return arr[n-1][m-1]
      
  

n,m = map(int,input().split())
arr = []
for _ in range(n):
  arr.append(list(map(int,input().strip())))
print(bfs(0,0))