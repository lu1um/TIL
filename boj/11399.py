N = int(input())

P = sorted(list(map(int, input().split())))

result = 0
wait = 0
for i in P:
    wait += i
    result += wait
print(result)
