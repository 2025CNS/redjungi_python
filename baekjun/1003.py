t = int(input())


def fibo(n):
    for i in range(2,n+1):
        for j in range(2):
            dp[i][j] = dp[i-1][j]+dp[i-2][j]
    return dp[n][0],dp[n][1]
    
result = []
for i in range(t):
    num = int(input())
    dp = [[0] * 2 for _ in range(num+1)]
    dp[0][0],dp[0][1] = 1,0
    if num > 0:
        dp[1][1],dp[1][0] = 1,0
    result.append(fibo(num))

for zero, one in result:
    print(zero, one)



