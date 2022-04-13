import sys
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr_sum = list()

for row in arr:
    arr_sum.append(row[:])

for i in range(N):
    for j in range(N):
        if i==0 and j==0:
            pass
        elif i==0:
            arr_sum[0][j] += arr_sum[0][j-1]
        elif j==0:
            arr_sum[i][0] += arr_sum[i-1][0]
        else:
            arr_sum[i][j] += arr_sum[i-1][j] + sum(arr[i][:j])

for _ in range(M):
    si, sj, ei, ej = map(int, sys.stdin.readline().split())
    if si == 1 and sj == 1:
        result = arr_sum[ei-1][ej-1]
    elif si == 1:
        result = arr_sum[ei-1][ej-1] - arr_sum[ei-1][sj-2]
    elif sj == 1:
        result = arr_sum[ei-1][ej-1] - arr_sum[si-2][ej-1]
    else:
        result = arr_sum[ei-1][ej-1] - arr_sum[si-2][ej-1] - arr_sum[ei-1][sj-2] + arr_sum[si-2][sj-2]
    print(result)