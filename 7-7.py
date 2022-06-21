import sys
input = sys.stdin.readline

N, M = map(int, input().split())
rc = list(map(int, input().split()))
start = 0
end = max(rc)

answer = 0
while start <= end:
    total = 0 # 잘린 길이

    mid = (start+end) // 2 # 절단기의 길이
    for r in rc:
        # 잘린 떡의 길이 합
        if r > mid:
            total += (r-mid)
        
    # 양이 적으면 더 많이 자름(왼쪽)
    if total < M:
        end = mid - 1
    # 양이 같거나 많으면 더 적게 자름(오른쪽)
    else:
        answer = mid # 최대한 덜 잘랐을 때가 정답이며, 최적해가 나올 때 마다 갱신됨
        start = mid + 1

print(answer)
