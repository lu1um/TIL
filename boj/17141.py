import sys
sys.stdin = open('input.txt')

from itertools import combinations
from collections import deque
from copy import deepcopy

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
cells = [list(map(int, input().split())) for _ in range(N)]

virus = list()
blank = 0
for i in range(N):
    for j in range(N):
        if cells[i][j] == 2:
            virus.append((i, j))
            blank += 1
            cells[i][j] = 0
        elif cells[i][j] == 0:
            blank += 1

min_time = 101
cases = combinations(virus, M)
for case in cases:
    arr = deepcopy(cells)
    for i, j in case:
        arr[i][j] = 1
    queue = deque(case)
    fill = M
    while queue:
        i, j = queue.popleft()
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<N and 0<=dj<N:
                if arr[di][dj] == 0:
                    arr[di][dj] = arr[i][j] + 1
                    queue.append((di, dj))
                    fill += 1
    if fill < blank:
        continue
    time = 0
    for row in arr:
        time = max(time, *row)
    if time < min_time:
        min_time = time
if min_time == 101:
    print(-1)
else:
    print(min_time-1)