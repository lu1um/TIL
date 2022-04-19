from collections import deque

N = int(input())

queue = deque([(N, 0)])
while queue:
    n, i = queue.popleft()
    if n == 1:
        break
    if n % 3 == 0:
        queue.append((n//3, i+1))
    elif n % 2 == 0:
        queue.append((n//2, i+1))
    queue.append((n-1, i+1))
print(i)