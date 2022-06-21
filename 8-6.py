N = int(input())
dp = [0] * N
lst = list(map(int, input().split()))

# 첫 두칸을 통해 Bottom-Up 방식의 Dynamic Programming 진행
dp[0] = lst[0]
dp[1] = max(lst[0], lst[1]) # 첫 두 칸에서는 합을 구할 수 없으니, 둘 중 최대 값으로 진행

# 이런 식으로 올라가면 이전의 최대 합과 이후의 값들을 비교하며 답을 구할 수 있음.
for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + lst[i]) # 이전까지의 합이 더 크냐, 이이전까지의 합과 현재 위치의 합이 더 크냐

print(dp[N-1])
