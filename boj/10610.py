N = list(input())
N.sort(reverse=True)

number = -1
if N[-1] == '0':
    n = int(''.join(N[:-1]))
    if n % 3 == 0:
        number = ''.join(N)
print(number)

