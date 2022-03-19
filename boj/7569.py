import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [[0, 0, -1], [0, 0, 1], [0, -1, 0], [0, 1, 0], [-1, 0, 0], [1, 0 ,0]]

M, N, H = map(int, input().split())
tomato = list()
queue = deque(list())

for i in range(H):
    temp = list()
    for j in range(N):
        temp.append(list(map(int, sys.stdin.readline().split())))
        for k in range(M):
            if temp[j][k] == 1:
                queue.append([i, j, k])
    tomato.append(temp)

while queue:
    h, y, x = queue.popleft()

    for d in DELTA:
        dh = h+d[0]
        dx = x+d[1]
        dy = y+d[2]
        if dh >= 0 and dh < H and dx >= 0 and dx < M and dy >= 0 and dy < N:
            if tomato[dh][dy][dx] == 0:
                queue.append([dh, dx, dy])
                tomato[dh][dy][dx] = tomato[h][y][x]+1

days = 0
for height in tomato:
    for row in height:
        for cell in row:
            if cell == 0:
                days = -1
                break
            days = max(days, max(days, cell))
        if days == -1:
            break
    if days == -1:
        break
print(days)