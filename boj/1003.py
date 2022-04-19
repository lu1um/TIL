def fibonacci(n):
    global dp
    if n == 0:
        dp[0] = 0
        return 0
    elif n == 1:
        dp[1] = 1
        return 1
    if dp[n]:
        return dp[n]
    else:
        dp[n] = fibonacci(n-1) + fibonacci(n-2)
        return dp[n]

T = int(input())
for tc in range(T):
    N = int(input())
    dp = [0] * 41
    if N == 0:
        print(1, 0)
    elif N == 1:
        print(0, 1)
    else:
        fibonacci(N)
        print(dp[N-1], dp[N])