import sys
sys.stdin = open('input.txt')

def getHoney(worker1, worker2):
    global max_honey, M, C
    price1 = 0
    price2 = 0
    for i in range(2**M):
        honey = 0
        price = 0
        for j in range(M):
            if i & 1<<j:
                price += worker1[j] ** 2
                honey += worker1[j]
            if honey > C:
                break
        else:
            if price > price1:
                price1 = price
    for i in range(2**M):
        honey = 0
        price = 0
        for j in range(M):
            if i & 1<<j:
                price += worker2[j] ** 2
                honey += worker2[j]
            if honey > C:
                break
        else:
            if price > price2:
                price2 = price
    if price1 + price2 > max_honey:
        max_honey = price1 + price2

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    hive = [list(map(int, input().split())) for _ in range(N)]

    max_honey = 0
    for i in range(N):
        for j in range(N-M+1):
            worker1 = hive[i][j:j+M]
            if j+M+M <= N:
                for y in range(j+M, N-M+1):
                    worker2 = hive[i][y:y+M]
                    getHoney(worker1, worker2)
            for x in range(i+1, N):
                for y in range(N-M+1):
                    worker2 = hive[x][y:y+M]
                    getHoney(worker1, worker2)

    print(f'#{tc} {max_honey}')