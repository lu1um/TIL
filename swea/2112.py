import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]

    print(f'#{tc} {arr}')