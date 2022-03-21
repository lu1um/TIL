from math import sqrt

M, N = map(int, input().split())

for num in range(M, N+1):
    if num != 1 and num % 2:
        for deno in range(3, int(sqrt(num))+1, 2):
            if num % deno == 0:
                break
        else:
            print(num)
    elif num == 2:
        print(num)

        # 1 2 3 4 5 6 7 8 9
        #   p p   p   p