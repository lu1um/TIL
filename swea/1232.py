import sys
sys.stdin = open('input.txt')

def main():
    for tc in range(1, 11):
        N = int(input())
        tree = dict()
        for _ in range(N):
            tree.update(receive(input().split()))
        traversal = Traversal(tree)
        traversal.postOrder(1)
        print(f'#{tc} {int(traversal.stack[0])}')

def receive(ls):
    node, ch, *path = tuple(ls)
    return { int(node): [ch, list(map(int, path))] }

class Traversal:
    def __init__(self, tree):
        self.tree = tree
        self.stack = list()
        self.calculate = {
            '+': add,
            '-': sub,
            '*': mul,
            '/': div,
        }

    def postOrder(self, v):
        node = self.tree[v]
        if node[1]:
            self.postOrder(node[1][0])
            self.postOrder(node[1][1])
            right = float(self.stack.pop())
            left = float(self.stack.pop())
            self.calculate[node[0]](self.stack, left, right)
        else:
            self.stack.append(node[0])

def add(stack, left, right):
    stack.append(left+right)

def sub(stack, left, right):
    stack.append(left-right)

def mul(stack, left, right):
    stack.append(left*right)

def div(stack, left, right):
    stack.append(left/right)

if __name__ == '__main__':
    main()