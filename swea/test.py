import sys
sys.stdin = open('input.txt')

def main():
    for tc in range(1, 11):
        N = int(input())
        formular = input()
        isp = {'(': 0, '+': 1, '*': 2}
        icp = {'(': 3, '+': 1, '*': 2, ')': -1}

        postfix = list()
        stack = Stack()
        for token in formular:
            if token not in icp.keys():
                postfix.append(int(token))
            else:
                if stack.empty:
                    stack.push(token)
                else:
                    top_isp = isp[stack.peek()]
                    token_icp = icp[token]
                    if token_icp == -1:
                        temp = stack.pop()
                        while not temp == '(':
                            postfix.append(temp)
                            temp = stack.pop()
                    elif token_icp > top_isp:
                        stack.push(token)
                    else:
                        while token_icp <= top_isp:
                            postfix.append(stack.pop())
                            top_isp = isp[stack.peek()]
                        stack.push(token)

        for token in postfix:
            if token not in icp.keys():
                stack.push(token)
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.push(left + right)
                elif token == '-':
                    stack.push(left - right)
                elif token == '*':
                    stack.push(left * right)
                elif token == '/':
                    stack.push(left / right)

        print(f'#{tc} {stack.peek()}')


class Stack(list):
    def __init__(self):
        self.top = -1

    @property
    def empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def peek(self):
        if self.empty:
            return None
        else:
            return self[self.top]

    def push(self, item):
        self.top += 1
        self.append(item)

    def pop(self):
        if self.empty:
            return None
        else:
            self.top -= 1
            return super().pop()


if __name__ == '__main__':
    main()