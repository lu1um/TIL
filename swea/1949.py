import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = ((0, 1), (0, -1), (1, 0), (-1, 0))

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]

    highest = 0
    for row in mountain:
        highest = max(highest, *row)

    tops = list()
    for i in range(N):
        for j in range(N):
            if mountain[i][j] == highest:
                tops.append((i, j))

    longest = 0
    for x in range(N):
        for y in range(N):
            for cut in range(1, K+1):
                mountain[x][y] -= cut
                for top in tops:
                    queue = deque([(top[0], top[1], 1)])
                    while queue:
                        i, j, distance = queue.popleft()
                        if distance > longest:
                            longest = distance
                        for d in DELTA:
                            di = i + d[0]
                            dj = j + d[1]
                            if 0<=di<N and 0<=dj<N:
                                if mountain[di][dj] < mountain[i][j]:
                                    queue.append((di, dj, distance+1))
                mountain[x][y] += cut
    print(f'#{tc} {longest}')
