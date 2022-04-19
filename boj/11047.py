N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

result = 0
idx = N-1
while K > 0:
    coin = K // coins[idx]
    result += coin
    K -= coins[idx] * coin
    idx -= 1
print(result)