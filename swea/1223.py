import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    tokens = input()

    postfix = list()
    stack = list()
    for token in tokens:
        if token != '+' and token != '*':
            postfix.append(int(token))
        else:
            if len(stack) == 0:
                stack.append(token)
            else:
                if token == '+':
                    stack.append(token)
                elif token == '*':
