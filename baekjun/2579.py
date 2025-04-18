t = int(input())

if t == 0:
  print(0)
else:
  stairs = []
  for i in range(t):
    stairs.append(int(input()))
  dp = [[0] * 2 for _ in range(t+1)]

  dp[1][0],dp[1][1] = stairs[0],stairs[0]
  if t >= 2:
        dp[2][0],dp[2][1] = stairs[1],stairs[0]+stairs[1]
  for i in range(3,t+1):
    dp[i][0] = max(dp[i-2][0],dp[i-2][1])+stairs[i-1]
    dp[i][1] = dp[i-1][0]+stairs[i-1]
  print(max(dp[t][0],dp[t][1]))
