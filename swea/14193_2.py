import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, T+1):
    X, Y = map(int, input().split())
    arr = [list(input()) for _ in range(Y)]

    nodes = list()
    nodes_count = 0
    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 'A':
                nodes.append((i, j))
                nodes_count += 1
            elif arr[i][j] == 'S':
                nodes.append((i, j))
                nodes[0], nodes[-1] = nodes[-1], nodes[0]
                nodes_count += 1
    stack = [nodes[0]]
    cable = 0
    while True:
        queue = deque(stack)
        visited = [[-1]*X for _ in range(Y)]
        for i, j in stack:
            visited[i][j] = 0

        while queue:
            i, j = queue.popleft()
            if visited[i][j] and (i, j) in nodes:
                stack.append((i, j))
                cable += visited[i][j]
                break
            for d in DELTA:
                di = i + d[0]
                dj = j + d[1]
                if 0<=di<X and 0<=dj<Y and visited[di][dj] == -1:
                    if arr[di][dj] != '#':
                        queue.append((di, dj))
                        visited[di][dj] = visited[i][j] + 1
        else:
            break

    print(cable)