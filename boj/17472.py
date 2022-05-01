import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

islands = [[], []]
island_number = 2
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue = deque([(i, j)])
            arr[i][j] = island_number
            island = [(i, j)]
            while queue:
                x, y = queue.popleft()
                for d in DELTA:
                    dx = x + d[0]
                    dy = y + d[1]
                    if 0<=dx<N and 0<=dy<M:
                        if arr[dx][dy] == 1:
                            arr[dx][dy] = island_number
                            island.append((dx, dy))
                            queue.append((dx, dy))
            islands.append(island)
            island_number += 1

island_count = island_number-2
bridges = [[10] * island_count for _ in range(island_count)]
for num in range(2, island_number):
    island = islands[num]
    for land in island:
        i, j = land
        for d in DELTA:
            length = 1
            connect = 0
            while True:
                di = i + d[0] * length
                dj = j + d[1] * length
                if 0<=di<N and 0<=dj<M:
                    if arr[di][dj] == 0:
                        length += 1
                        continue
                    elif arr[di][dj] != num and length > 2:
                        connect = arr[di][dj]
                        break
                length = 10
                break
            if connect:
                if length-1 < bridges[num-2][connect-2]:
                    bridges[num-2][connect-2] = length-1

# MST
answer = 10*6
for start in range(island_count):
    connected = [False] * island_count
    connected[start] = True
    temp = 0
    while False in connected:
        min_length = 10
        connecting = -1
        for i in range(island_count):
            if connected[i]:
                for j in range(island_count):
                    if not connected[j]:
                        if bridges[i][j] < min_length:
                            min_length = bridges[i][j]
                            connecting = j
        if connecting == -1:
            break
        else:
            connected[connecting] = True
            temp += min_length
    else:
        if temp < answer:
            answer = temp
if answer == 10*6:
    print(-1)
else:
    print(answer)
