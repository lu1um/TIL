import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]

N, K = map(int, input().split())
queue = list()
visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v:
            queue.append((v, i, j, 0))
            visited[i][j] = v
S, X, Y = map(int, input().split())

queue.sort()
queue = deque(queue)
while queue:
    virus, i, j, time = queue.popleft()
    if time == S:
        break
    for d in DELTA:
        di = i + d[0]
        dj = j + d[1]
        if 0<=di<N and 0<=dj<N:
            if visited[di][dj] == 0:
                queue.append((virus, di, dj, time+1))
                visited[di][dj] = virus
print(visited[X-1][Y-1])
