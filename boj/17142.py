import sys
sys.stdin = open('input.txt')

from itertools import combinations
from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

virus = list()
blank = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 0:
            blank += 1
        elif arr[i][j] == 2:
            virus.append((i, j))

min_time = 2500
cases = combinations(virus, M)
for case in cases:
    queue = deque(case)
    visited = [[-1]*N for _ in range(N)]
    for c in case:
        visited[c[0]][c[1]] = 0
    remain = blank
    while queue:
        if remain <= 0:
            remain = 0
            break
        i, j = queue.popleft()
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<N and 0<=dj<N and visited[di][dj] == -1:
                if arr[di][dj] != 1:
                    queue.append((di, dj))
                    visited[di][dj] = visited[i][j] + 1
                    if (di, dj) not in virus:
                        remain -= 1
    if remain:
        continue
    else:
        taken_time = 0
        for v in visited:
            taken_time = max(taken_time, *v)
        if taken_time < min_time:
            min_time = taken_time
if min_time == 2500:
    min_time = -1
print(min_time)