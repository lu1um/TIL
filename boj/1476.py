E, S, M = map(int, input().split())

e = 1
s = 1
m = 1
year = 1
while not (e == E and s == S and m == M):
    if e == 15:
        e = 1
    else:
        e += 1
    if s == 28:
        s = 1
    else:
        s += 1
    if m == 19:
        m = 1
    else:
        m += 1
    year += 1
print(year)