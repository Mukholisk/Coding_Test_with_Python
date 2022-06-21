from re import M


def binarysearch(lst, s, e, target):
    if s > e:
        return -1

    m = (s+e) // 2

    if lst[m] == target:
        return m
    elif lst[m] > target:
        return binarysearch(lst, s, m-1, target)
    else:
        return binarysearch(lst, m+1, e, target)

n, target = input().split()
n = int(n)
lst = list(input().split())

print(binarysearch(lst, 0, n-1, target))
