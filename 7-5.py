# 이진탐색 + etc -> 탐색 범위가 2000만이 넘어가거나, 처리해야 할 데이터의 개수나 값이 1000만 단위 이상이 될 경우 사용
def binarysearch(lst, s, e, target):
    if s > e:
        return "no"
    
    m = (s+e) // 2
    if lst[m] == target:
        return 'yes'
    elif target < lst[m]:
        return binarysearch(lst, s, m-1, target)
    else:
        return binarysearch(lst, m+1, e, target)

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

n_lst.sort()
for m in m_lst:
    print(binarysearch(n_lst, 0, N-1, m), end=' ')
