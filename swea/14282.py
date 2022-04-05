import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dp = [[float('inf')]*N for _ in range(N)]
    dp[0][0] = 0

    queue = deque([(0, 0)])
    while queue:
        i, j = queue.popleft()
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<N and 0<=dj<N:
                height = 1
                if arr[di][dj] > arr[i][j]:
                    height += arr[di][dj] - arr[i][j]
                fuel = dp[i][j] + height
                if fuel < dp[di][dj]:
                    dp[di][dj] = fuel
                    queue.append((di, dj))
    print(f'#{tc} {dp[N-1][N-1]}')

