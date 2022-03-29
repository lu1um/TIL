import sys
sys.stdin = open('input.txt')

def add(left, right):
    return left+right
def sub(left, right):
    return left-right
def mul(left, right):
    return left*right
def div(left, right):
    return left//right

CALCULATE = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

T = int(input())
for tc in range(1, T+1):
    forth = input().split()
    stack = list()
    result = 0
    for token in forth:
        if token == '.':
            if len(stack) == 1:
                result = stack[0]
            else:
                result = 'error'
            break
        try:
            if token in CALCULATE.keys():
                right = stack.pop()
                left = stack.pop()
                stack.append(CALCULATE[token](left, right))
            else:
                stack.append(int(token))
        except:
            result = 'error'
            break
    print(f'#{tc} {result}')