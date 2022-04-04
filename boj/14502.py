import sys
from time import time
sys.stdin = open('input.txt')
start = time()

from itertools import combinations

DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
blank = []
virus = []
blank_count = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            blank.append((i, j))
            blank_count += 1
        elif arr[i][j] == 2:
            virus.append((i, j))

blank_comb = combinations(blank, 3)
max_cell = 0
for bk in blank_comb:
    cell = blank[:]
    cell_count = blank_count-3
    for b in bk:
        cell.remove(b)
    viruses = virus[:]
    while viruses:
        i, j = viruses.pop()
        for d in DELTA:
            didj = (i+d[0], j+d[1])
            if didj in cell:
                viruses.append(didj)
                cell.remove(didj)
                cell_count -= 1
        if cell_count <= max_cell:
            break
    else:
        max_cell = cell_count
print(max_cell)

print('time : ', time()-start)