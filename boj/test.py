arr = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]
def bingo():
    cnt = 0
    for i in range(5):
        for j in range(5): #사회자가 부르는 숫자
            bingo = 0
            cnt += 1
            for k in range(5):
                for l in range(5): #빙고판에 있는지 맞춰보고
                    if arr[k][l] == arr2[i][j]:
                        arr[k][l] = 0

            for m in range(5): #가로줄
                if arr[m] == [0, 0, 0, 0, 0]:
                    bingo += 1

            for m in range(5): #세로줄
                bin = 0
                for n in range(5):
                    if arr[n][m] == 0:
                        bin += 1
                        if bin == 5:
                            bingo += 1

            bin = 0
            for m in range(5): #대각
                if arr[m][m] == 0:
                    bin += 1
                    if bin == 5:
                        bingo += 1
            bin = 0
            for m in range(5): #역대각
                if arr[m][4-m] == 0:
                    bin += 1
                    if bin == 5:
                        bingo += 1

            if bingo >= 3:
                return cnt
print(bingo())