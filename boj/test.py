def dfs(k, i, j, num):
    global res
    if num==n: # q를 n개만큼 놓았을때, 종료
        res += 1
        return
    elif k==n*n:
        return

    for di, dj in ((0, 1),(0,-1),(1, 0),(-1,0),(-1,-1), (1, 1), (1, -1), (-1, 1)):
        # 새로 간 위치에서 퀸이 있는 곳을 공격하면 안되므로
        # 새로간 dfs에서 둘러볼 방향을 설정해준다.
        for x in range(1, n):
            ni, nj = i+di*x, j+dj*x
            if 0<=ni<n and 0<=nj<n:
                if arr[ni][nj]==0:
                    arr[ni][nj] = 1
                    dfs(k+1, ni, nj, num+1)
                elif arr[ni][nj]==1:
                    dfs(k+1, ni, nj, num)

n = int(input())
arr = [[0]*n for _ in range(n)]
# 서로를 공격할 수 없게 놓아라 !
res = 0
for i in range(n):
    for j in range(n):
        dfs(1, i, j, 0)
print(res)