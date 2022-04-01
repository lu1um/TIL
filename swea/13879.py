import sys
sys.stdin = open('input.txt')

def game(lst):
    if len(lst) == 1:
        return lst[0]
    j = len(lst)-1
    left = game(lst[:j//2 + 1])
    right = game(lst[j//2 + 1:])
    left_card = cards[left]
    right_card = cards[right]
    if left_card == 1:
        if right_card == 1 or right_card == 3:
            return left
        else:
            return right
    elif left_card == 2:
        if right_card == 2 or right_card == 1:
            return left
        else:
            return right
    else:
        if right_card == 3 or right_card == 2:
            return left
        else:
            return right

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split())) # 2 1 3 1 2 1
    player = list(range(N)) # 0 1 2 3 4 5
    winner = game(player)
    print(f'#{tc} {winner+1}')
