import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = numbers[i] * numbers[j]
            if num < max_num:
                continue
            str_num = str(num)
            for k in range(len(str_num)-1):
                if int(str_num[k]) > int(str_num[k+1]):
                    break
            else:
                max_num = num
    print(f'#{tc} {max_num}')