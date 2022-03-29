import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    player = {
        0: [],
        1: [],
    }
    winner = 0
    for i in range(12):
        turn = player[i % 2]
        turn.append(cards[i])
        if len(turn) >= 3:
            turn.sort()
            old_card = turn[0]
            isRun = 0
            isPair = 0
            for card in turn[1:]:
                if card == old_card:
                    if isPair:
                        isPair = 2
                        break
                    else:
                        isPair = 1
                else:
                    isPair = 0
                    if card == old_card+1:
                        if isRun:
                            isRun = 2
                            break
                        else:
                            isRun = 1
                    else:
                        isRun = 0
                old_card = card
            if isRun == 2 or isPair == 2:
                winner = (i % 2) + 1
                break
    print(f'#{tc} {winner}')