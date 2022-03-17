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

    def postOrder(self, v):
        node = self.tree[v]
        if node[1]:
            self.postOrder(node[1][0])
            self.postOrder(node[1][1])
            right = float(self.stack.pop())
            left = float(self.stack.pop())
            if node[0] == '+':
                self.stack.append(left+right)
            elif node[0] == '-':
                self.stack.append(left-right)
            elif node[0] == '*':
                self.stack.append(left*right)
            elif node[0] == '/':
                self.stack.append(left/right)
        else:
            self.stack.append(node[0])
            return

if __name__ == '__main__':
    main()