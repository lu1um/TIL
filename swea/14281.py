import sys
sys.stdin = open('input.txt')

import heapq

def find(x):
    if not x == parent[x]:
        return find(parent[x])
    return x

def merge(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    parent = list(range(V+1))
    graph = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        heapq.heappush(graph, (w, s, e))

    weight = 0
    while graph:
        w, s, e = heapq.heappop(graph)
        if not find(s) == find(e):
            weight += w
            merge(s, e)
    print(f'#{tc} {weight}')