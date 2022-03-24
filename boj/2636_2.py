import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def freshAir(q, N, M):
    for i in range(1, N-1):
        q.append([i, 0])
        q.append([i, M-1])
    for i in range(1, M-1):
        q.append([0, i])
        q.append([N-1, i])


N, M = map(int, input().split())
cheese = [list(map(int, input().split())) for _ in range(N)]

queue = deque()
result = 0
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if cheese[i][j] == 1:
            result += 1
remain_cheese = result
hour = 2
while remain_cheese:
    result = remain_cheese
    freshAir(queue, N, M)
    while queue:
        temp = queue.popleft()
        for d in DELTA:
            di = temp[0]+d[0]
            dj = temp[1]+d[1]
            if 0<=di<N and 0<=dj<M:
                this = cheese[di][dj]
                if this == hour or this == 0:
                    cheese[di][dj] = hour+1
                    queue.append([di, dj])
                elif this == 1:
                    cheese[di][dj] = hour+1
    remain_cheese = 0
    for i in range(1, N - 1):
        for j in range(1, M - 1):
            if cheese[i][j] == 1:
                remain_cheese += 1
    hour += 1

print(f'{hour-2}\n{result}')