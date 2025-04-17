import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
m = len(s1)
n = len(s2)
dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1,m+1):
  for k in range(1,n+1):
    if s1[i-1] == s2[k-1]:
      dp[i][k] = 1+dp[i-1][k-1]
    else:
      dp[i][k] = max(dp[i][k-1],dp[i-1][k])

result = []
x = m
y = n
while x > 0 and y > 0:
  if dp[x][y] == dp[x][y - 1]:
    y -= 1
  elif dp[x][y] == dp[x - 1][y]:
    x -= 1
  elif s1[x - 1] == s2[y - 1]:
    result.append(s1[x - 1])
    x -= 1
    y -= 1
  else:
    y -= 1 
result.reverse()
print("".join(result))
    
  
    
    
  