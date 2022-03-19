import sys
sys.stdin = open('input.txt')

def main():
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))

        i = abs(M-N)
        if M > N:
            result = solver(A, B, i, N)
        else:
            result = solver(B, A, i, M)
        print(f'#{tc} {result}')

def solver(A, B, k, size):
    max_mul = 0
    while k >= 0:
        temp = 0
        for i in range(size):
            temp += A[i] * B[i+k]
        if temp > max_mul:
            max_mul = temp
        k -= 1
    return max_mul

if __name__ == '__main__':
    main()