import sys
sys.stdin = open('input.txt')

def main():
    for tc in range(1, 11):
        N = int(input())
        tree = dict()
        for _ in range(N):
            tree.update(receive(input().split()))
        traversal = Traversal(tree)
        print(f'#{tc}', end=' ')
        traversal.inOrder(1)
        print()

def receive(ls):
    node, ch, *path = tuple(ls)
    path_list = list(map(int, path))
    return { int(node): [ch, path_list] }   # { node_num: [alphabet, [left_child_num, right_child_num]] }

class Traversal:
    def __init__(self, tree):
        self.tree = tree

    def inOrder(self, node):
        node_data = self.tree[node]
        if node_data[1]:
            self.inOrder(node_data[1][0])   # left child
            print(node_data[0], end='')     # parent
            if len(node_data[1]) == 2:      # if right child is exist
                self.inOrder(node_data[1][1])   # right child
            return
        else:       # if leaf node
            print(node_data[0], end='')
            return

if __name__ == '__main__':
    main()