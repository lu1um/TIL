import sys
sys.stdin = open('input.txt')

PASSWORD = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9,
}

HEX = {
    '0':'0000', '1':'0001', '2':'0010', '3':'0011',
    '4':'0100', '5':'0101', '6':'0110', '7':'0111',
    '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
    'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111',
}

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    codes = set([input().strip() for _ in range(N)])
    binary = str()
    visited = list()
    for code in codes:
        binary = ''
        for c in code:
            binary += HEX[c]
        a = 0
        b = 0
        c = 0
        binary = binary.rstrip('0')
        i = len(binary)
        decimal = [0] * 8
        d_idx = 7
        while i > 0:
            i -= 1
            if binary[i] == '1' and b == 0 and a == 0:
                c += 1
            elif binary[i] == '0' and a == 0 and c > 0:
                b += 1
            elif binary[i] == '1' and b > 0 and c > 0:
                a += 1
            elif binary[i] == '0' and a > 0 and b > 0 and c > 0:
                deno = min(a, b, c)
                key = (a//deno, b//deno, c//deno)
                decimal[d_idx] = PASSWORD[key]
                a = 0
                b = 0
                c = 0
                d_idx -= 1
            if d_idx == -1:
                d_idx = 7
                odd_sum = (decimal[0] + decimal[2] + decimal[4] + decimal[6]) * 3
                even_sum = decimal[1] + decimal[3] + decimal[5]
                parity = odd_sum + even_sum + decimal[7]
                if parity % 10 == 0 and decimal not in visited:
                    result += sum(decimal)
                    visited.append(decimal)
                decimal = [0] * 8
    print(f'#{tc} {result}')

