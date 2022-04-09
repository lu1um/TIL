import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

x, y = map(lambda z: int(z)-1, input().split())
passengers = list()
goals = list()
for _ in range(M):
    sx, sy, ex, ey = map(int, input().split())
    passengers.append((sx-1, sy-1))
    goals.append((ex-1, ey-1))


print(passengers)
print(goals)

result = 0
here_x = x
here_y = y
while goals:
    queue = deque([(here_x, here_y, 0)])
    target = M
    min_distance = 41
    visited = [[False] * N for _ in range(N)]
    while queue:
        i, j, distance = queue.popleft()
        visited[i][j] = True
        if distance > min_distance:
            break
        if (i, j) in passengers:
            new_target = passengers.index((i, j))
            if new_target < target:
                target = new_target
                min_distance = distance
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0<=di<N and 0<=dj<N and not visited[di][dj]:
                if arr[di][dj] == 0:
                    queue.append((di, dj, distance+1))
    else:
        result = -1
        break
    fuel -= min_distance

    print(f'target : {target}')

    goal_i, goal_j = goals[target]
    car_i, car_j = passengers[target]
    queue = deque([(car_i, car_j, 0)])
    distance = 0
    visited = [[False] * N for _ in range(N)]
    while queue:
        i, j, distance = queue.popleft()
        visited[i][j] = True
        if (i, j) == (goal_i, goal_j):
            break
        for d in DELTA:
            di = i + d[0]
            dj = j + d[1]
            if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:
                if arr[di][dj] == 0:
                    queue.append((di, dj, distance + 1))
    else:
        result = -1
        break
    fuel -= distance
    if fuel < 0:
        result = -1
        break
    else:
        fuel += distance * 2
        here_x, here_y = goals[target]
        del passengers[target]
        del goals[target]
else:
    result = fuel
print(result)
