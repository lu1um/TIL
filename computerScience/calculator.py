#!/usr/bin/env python

def main():
    formular = '(6+5*(2-8)/2)'
    isp = {'(':0, '+':1, '-':1,'*':2, '/':2}
    icp = {'(':3, '+':1, '-':1,'*':2, '/':2}

    postfix = list()
    stack = Stack()
    for token in formular:
        if token not in isp.keys():
            postfix.append(token)
        else:
            if stack.empty:
                stack.push(token)
            else:
                top_isp = isp[stack.peek()]
                token_icp = icp[token]
                if token_icp > top_isp:
                    stack.push(token)
                elif token == ')':
                    temp = stack.pop()
                    while not temp == '(':
                        postfix.append(temp)
                        temp = stack.pop()
                else:
                    while token_icp <= top_isp:
                        postfix.append(stack.pop())
                    stack.push(token)

    print(stack)
    print(postfix)



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