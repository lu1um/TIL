import sys
sys.stdin = open('input.txt')

def quickSort(ls):
    if len(ls) > 1:
        pivot, ls = partition(ls)
        left = quickSort(ls[:pivot])
        right = quickSort(ls[pivot:])
    else:
        return ls
    return left+right


def partition(ls):
    M = len(ls)
    i = -1
    pivot = ls[M-1]
    for j in range(M-1):
        if ls[j] <= pivot:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    ls[M-1], ls[i+1] = ls[i+1], ls[M-1]
    print(ls)
    return i+1, ls

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst = quickSort(lst)
    print(f'#{tc} {lst[N//2]}')