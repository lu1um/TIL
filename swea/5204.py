import sys
sys.stdin = open('input.txt')

from collections import deque

def mergeSort(ls):
    global counter
    M = len(ls)
    if M > 1:
        left = deque(mergeSort(ls[:M//2]))
        right = deque(mergeSort(ls[M//2:]))

        if left[-1] > right[-1]:
            counter += 1

        sorted_ls = list()
        while left or right:
            if left and right:
                if left[0] <= right[0]:
                    sorted_ls.append(left.popleft())
                else:
                    sorted_ls.append(right.popleft())
            elif left:
                sorted_ls.extend(left)
                left = []
            elif right:
                sorted_ls.extend(right)
                right = []
        return sorted_ls
    else:
        return ls

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    counter = 0
    lst = mergeSort(lst)
    print(f'#{tc} {lst[N//2]} {counter}')
