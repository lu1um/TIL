import sys
sys.stdin = open('input.txt')

def main():
    T = int(input())
    for tc in range(1, T+1):
        binary = list(input())
        ternary = list(input())

        result = solver(binary, ternary)
        print(f'#{tc} {result}')

def decimal(num, base):
    _decimal = 0
    exp = 0
    while num:
        n = num.pop()
        _decimal += int(n) * (base**exp)
        exp += 1
    return _decimal

def solver(binary, ternary):
    for i in range(len(binary)):
        fixed_bin = binary[:]
        if fixed_bin[i] == '0':
            fixed_bin[i] = '1'
        else:
            fixed_bin[i] = '0'

        for j in range(len(ternary)):
            fixed_ter = ternary[:]
            ter_case = ['0', '1', '2']
            del ter_case[int(fixed_ter[j])]
            for t in ter_case:
                fixed_ter[j] = t
                dec_bin = decimal(fixed_bin[:], 2)
                dec_ter = decimal(fixed_ter[:], 3)
                if dec_bin == dec_ter:
                    return dec_bin

if __name__ == '__main__':
    main()