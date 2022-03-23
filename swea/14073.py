import sys
sys.stdin = open('input.txt')   # 이진 탐색

def main():
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        tree = [0] * (N+1)
        traversal = Traversal()
        traversal.inOrder(tree, N, 1)

        print(f'#{tc} {tree[1]} {tree[N//2]}')

class Traversal:
    def __init__(self):
        self.num = 1

    def inOrder(self, tree, N, v):
        if v <= N:
            self.inOrder(tree, N, v*2)
            tree[v] = self.num
            self.num += 1
            self.inOrder(tree, N, v*2+1)
        return

if __name__ == '__main__':
    main()