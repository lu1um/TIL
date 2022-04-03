import sys
sys.stdin = open('input.txt')

import sys

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(visited, i, j, counter, _sum):
    global max_sum
    if _sum + max_num * (4-counter) < max_sum:
        return
    if counter == 4:
        max_sum = _sum
        return
    for d in DELTA:
        di = i + d[0]
        dj = j + d[1]
        if 0<=di<N and 0<=dj<M:
            if (di, dj) not in visited:
                if counter == 2:
                    dfs(visited+[(di, dj)], i, j, counter+1, _sum+arr[di][dj])
                dfs(visited+[(di, dj)], di, dj, counter+1, _sum+arr[di][dj])

N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
max_num = max(map(max, arr))
max_sum = 0
for i in range(N):
    for j in range(M):
        dfs([(i, j)], i, j, 1, arr[i][j])
print(max_sum)