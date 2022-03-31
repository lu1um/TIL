import sys
sys.stdin = open('input.txt')

LEFT = 1
RIGHT = 2

def binSearch(lst, target, direction):
    if lst:
        m = (len(lst)-1)//2
        middle = lst[m]
        if middle == target:
            return 1
        elif middle < target:
            if direction != RIGHT:
                return binSearch(lst[m+1:], target, RIGHT)
        else:
            if direction != LEFT:
                return binSearch(lst[:m], target, LEFT)
    return 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    counter = 0
    for b in B:
        counter += binSearch(A, b, 0)
    print(f'#{tc} {counter}')