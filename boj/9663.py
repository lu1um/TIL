DELTA = [-1, 0, 1]

def backTracking(queen, row):
    global counter
    if row == N+1:
        counter += 1
    for j in range(N):
        for d in DELTA:
            for x in range(1, row):
                check = (row-x, j + d*x)
                if check in queen:
                    return
        backTracking(queen+[(row, j)], row+1)

N = int(input())
counter = 0
backTracking([], 1)
print(counter)