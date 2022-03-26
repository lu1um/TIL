import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    dish = [[0]*N for _ in range(N)]
    for _ in range(K):
        y, x, amount, direction = map(int, input().split())
        dish[y][x] = [amount, direction]

    print(dish)