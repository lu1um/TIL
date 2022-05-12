import sys
from pprint import pprint
sys.stdin = open('input.txt')

from collections import deque

m, n = map(int, input().split())
k = int(input())
arr = [[[] for _ in range(m)] for _ in range(n)]
buses = dict()
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    buses[b] = []
    for y in range(y1-1, y2):
        for x in range(x1-1, x2):
            buses[b].append((x, y))
            arr[y][x].append(b)
sx, sy, dx, dy = map(lambda l: int(l)-1, input().split())
endBus = arr[dy][dx]
transfer = deque([])
visited = list()
cnt = 1
for e in endBus:
    visited.append(e)
    transfer.append((e, 1))
isEnd = False
while transfer:
    bus_num, cnt = transfer.popleft()
    for x, y in buses[bus_num]:
        if x == sx and y == sy:
            isEnd = True
            break
        for bus in arr[y][x]:
            if bus not in visited:
                visited.append(bus)
                transfer.append((bus, cnt+1))
    if isEnd:
        break
print(cnt)
