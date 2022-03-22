import sys
sys.stdin = open('input.txt')

class Tree:
    def __init__(self):
        self.node = [0] * 1001
        self.last = int()

    def setLast(self, L):
        self.last = L

    def getNode(self, v):
        return self.node[v]

    def addNode(self, v, num):
        self.node[v] = num

    def fillNode(self, L):
        for i in range(self.last, L-1, -1):
            if self.node[i] == 0:
                self.node[i] = self.node[i*2] + self.node[i*2+1]


T = int(input())
for tc in range(1, T+1):
    tree = Tree()
    N, M, L = map(int, input().split())
    tree.setLast(N)
    for i in range(M):
        node, num = map(int, input().split())
        tree.addNode(node, num)
    tree.fillNode(L)
    print(f'#{tc} {tree.getNode(L)}')