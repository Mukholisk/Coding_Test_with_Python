# Bottom-Up

dp = [0] * 1001
dp[1] = 1
dp[2] = 1

n = 250
for i in range(3, n+1):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n])