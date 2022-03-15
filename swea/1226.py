import sys
sys.stdin = open('input.txt')

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
DIR = [UP, LEFT, DOWN, RIGHT]

def main():
    for t in range(1, 11):
        tc = int(input())
        maze = [input() for _ in range(16)]

        i = 0
        j = 0
        for row in range(16):   # find start point
            for col in range(16):
                if maze[row][col] == '2':
                    i = row
                    j = col
                    break
            if i or j:
                break

        junction = [(0, 0), (i, j)]
        start_junc = findJunction(maze, i, j)
        head = start_junc.pop()
        junction_dir = [[], start_junc]
        isArrival = 0
        while junction:
            i += head[0]
            j += head[1]
            if maze[i][j] == '3':
                isArrival = 1
                break
            # 상하좌우 체크 junction이면 junction과 junction_dir에 추가
            path = findJunction(maze, i, j, head)
            if path:
                head = path.pop()
                if path:
                    junction.append((i, j))
                    junction_dir.append(path)
            # 만약 갈 길이 없다면, junction.pop으로 i, j 바꾸고 head를 junction_dir로
            else:
                heads = junction_dir[-1]
                if heads:
                    head = heads.pop()
                i, j = junction[-1]
                if not heads:
                    junction.pop()
                    junction_dir.pop()

        print(f'#{tc} {isArrival}')

def findJunction(maze, i, j, head=None):
    junction_dir = list()
    if head:
        tail = DIR[DIR.index(head)-2]
    else:
        tail = None
    for dir in DIR:
        if maze[i + dir[0]][j + dir[1]] == '0' or maze[i + dir[0]][j + dir[1]] == '3':
            if dir is tail:
                continue
            junction_dir.append(dir)
    return junction_dir

if __name__ == '__main__':
    main()
