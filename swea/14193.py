import sys
sys.stdin = open('input.txt')

from collections import deque

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

T = int(input())
for tc in range(1, T+1):
    X, Y = map(int, input().split())
    arr = [input() for _ in range(Y)]

    nodes = dict()
    nodes_position = dict()
    node_num = 1
    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 'A':
                nodes.update({ node_num: [] })
                nodes_position.update({ (i, j): node_num })
                node_num += 1
            elif arr[i][j] == 'S':
                nodes.update({ 0: [] })
                nodes_position.update({ (i, j): 0 })
    for i in range(node_num):
        nodes[i].extend([0]*(node_num))

    for node in nodes_position.keys():
        start_node = nodes_position.get(node)
        queue = deque([node])
        visited = [[-1]*X for _ in range(Y)]
        visited[node[0]][node[1]] = 0
        while queue:
            i, j = queue.popleft()
            isNode = nodes_position.get((i, j))
            if isNode is not None:
                nodes[start_node][isNode] = visited[i][j]
            for d in DELTA:
                di = i + d[0]
                dj = j + d[1]
                if 0<=di<X and 0<=dj<Y and visited[di][dj] == -1:
                    if arr[di][dj] != '#':
                        visited[di][dj] = visited[i][j] + 1
                        queue.append((di, dj))

    for i in range(node_num):
        print(nodes[i])

    connected = [False] * node_num
    connected[1] = True
    total_cable = 0
    cable = [nodes[1]]
    while False in connected:
        short_cable = 100
        cable_idx = 0
        for c in cable:
            for j in range(node_num):
                if c[j] != 0 and c[j] < short_cable:
                    short_cable = c[j]
                    cable_idx = j
        connected[cable_idx] = True
        cable.append(nodes[cable_idx])
        for c in cable:
            for idx in range(node_num):
                if connected[idx]:
                    c[idx] = 0
        total_cable += short_cable

    print(total_cable)
