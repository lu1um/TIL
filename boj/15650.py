def combination(idx, i, ls):
    if i == M:
        print(*ls)
    for j in range(idx, N):
        combination(j+1, i+1, ls+[j+1])

N, M = map(int, input().split())

combination(0, 0, [])
