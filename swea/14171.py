import sys
sys.stdin = open('input.txt')
# greedy

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            above = 10*13
            left = 10*13
            if i == 0 and j == 0:
                continue
            if 0<=i-1<N:
                above = mat[i-1][j]
            if 0<=j-1<N:
                left = mat[i][j-1]
            mat[i][j] += min(above, left)
    print(f'#{tc} {mat[N-1][N-1]}')
