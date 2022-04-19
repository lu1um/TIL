import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

count = 0
isBreak = False
while not isBreak:
    isBreak = True
    visited = [[False]*N for _ in range(N)]
    unions = list()
    peoples = list()
    for x in range(N):
        for y in range(N):
            if not visited[x][y]:
                queue = deque([(x, y)])
                union = list()
                people = 0
                union_number = 0
                visited[x][y] = True
                while queue:
                    i, j = queue.popleft()
                    union.append((i, j))
                    people += arr[i][j]
                    union_number += 1
                    for d in DELTA:
                        di = i + d[0]
                        dj = j + d[1]
                        if 0<=di<N and 0<=dj<N and visited[di][dj] == False:
                            if L <= abs(arr[i][j] - arr[di][dj]) <= R:
                                isBreak = False
                                queue.append((di, dj))
                                visited[di][dj] = True
                people_avg = people // union_number
                unions.append(union)
                peoples.append(people_avg)
    if isBreak:
        break
    count += 1
    for idx, union in enumerate(unions):
        people = peoples[idx]
        for x, y in union:
            arr[x][y] = people
print(count)
