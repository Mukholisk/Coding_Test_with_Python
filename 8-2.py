# Top-Down
import sys
sys.setrecursionlimit(10001)

dp = [0] * 10001

def fibo(n):
    if n <= 2:
        return 1
    
    if dp[n] != 0:
        return dp[n]
    
    dp[n] = fibo(n-2) + fibo(n-1)

    return dp[n]

print(fibo(7850))
