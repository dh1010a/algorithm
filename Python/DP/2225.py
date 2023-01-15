n, k = map(int, input().split())

dp = [[1 for i in range(k+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(2,k+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][k] % 1000000000)