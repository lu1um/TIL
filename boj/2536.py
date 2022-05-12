import sys
sys.stdin = open('input.txt')

m, n = map(int, input().split())
k = int(input())
x_buses = [[] for _ in range(n+1)]
y_buses = [[] for _ in range(m+1)]
for _ in range(k):
    b, x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        if y1 > y2:
            y_buses[x1].append((b, y2, y1))
        else:
            y_buses[x1].append((b, y1, y2))
    else:
        if x1 > x2:
            x_buses[y1].append((b, x2, x1))
        else:
            x_buses[y1].append((b, x1, x2))
sx, sy, dx, dy = map(int, input().split())


print(x_buses)
print(y_buses)