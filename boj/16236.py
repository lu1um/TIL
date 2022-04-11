import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, -1), (-1, 0), (1, 0), (0, 1)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

baby = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            baby = (i, j)
            arr[i][j] = 0
            break
    if baby:
        break

size = 2
eat = 0
second = 0
while True:
    queue = deque([baby])
    visited = [[-1]*N for _ in range(N)]
    visited[baby[0]][baby[1]] = 0
    isPrey = False
    prey = (20, 20)
    prey_distance = 41
    while queue:
        i, j = queue.popleft()
        if visited[i][j] > prey_distance:
            break
        if arr[i][j] != 0 and arr[i][j] < size:
            if i < prey[0]:
                isPrey = True
                prey = (i, j)
                prey_distance = visited[i][j]
            elif i == prey[0]:
                if j < prey[1]:
                    isPrey = True
                    prey = (i, j)
                    prey_distance = visited[i][j]
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<N and 0<=dj<N and visited[di][dj] == -1:
                if arr[di][dj] <= size:
                    queue.append((di, dj))
                    visited[di][dj] = visited[i][j] + 1
    if not isPrey:
        break
    arr[prey[0]][prey[1]] = 0
    eat += 1
    second += visited[prey[0]][prey[1]]
    baby = (prey[0], prey[1])
    if eat == size:
        size += 1
        eat = 0
print(second)