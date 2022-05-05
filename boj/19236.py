import sys
sys.stdin = open('input.txt')

DIRECTION = {
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1)
}

fishes = []
for i in range(4):
    fish_row = []
    row = list(map(int, input().split()))
    for j in range(4):
        fish_row.append([row[j*2], row[j*2+1]])
    fishes.append(fish_row)

