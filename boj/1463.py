n = int(input())

dp = [0]*(n+4)
dp[1] = 0  # idx 숫자로 맞춰줌
dp[2] = 1
dp[3] = 1

if n<4:
    print(dp[n])
else:
    for i in range(4, n+1):
        if i%3==0:
            dp[i] = min(dp[i-1]+1, dp[i//3]+1)
        if i%2==0:
            dp[i] = min(dp[i-1]+1, dp[i//2]+1)
        else:
            dp[i] = min(dp[i], dp[i-1]+1)
    print(dp[n])
print(dp)