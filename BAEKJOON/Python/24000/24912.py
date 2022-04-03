"""
Title : 카드 색칠
"""

import sys
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    cards = list(map(int ,input().split()))
    
    if N == 1:
        if cards[0]:
            print(cards[0])
        else:
            print(1)
    elif N == 2:
        if cards[0] and cards[0] == cards[1]:
            print(-1)
        else:
            if not cards[0]:
                if cards[1] == 1:
                    cards[0] = 2
                else:
                    cards[0] = 1
            if not cards[1]:
                if cards[0] == 1:
                    cards[1] = 2
                else:
                    cards[1] = 1
            print(*cards)
    else:
        if not cards[0] and N >= 2:
            if cards[1] == 1:
                cards[0] = 2
            else:
                cards[0] = 1
        if not cards[-1] and N >= 2:
            if cards[-2] == 1:
                cards[-1] = 2
            else:
                cards[-1] = 1
        for i in range(1, N - 1):
            if cards[i]:
                if cards[i] == cards[i - 1]:
                    print(-1)
                    break
                continue
            if cards[i + 1]:
                card = {1, 2, 3} - {cards[i - 1], cards[i + 1]}
                card = card.pop()
                cards[i] = card
            else:
                if cards[i - 1] == 1:
                    cards[i] = 2
                else:
                    cards[i] = 1
        else:
            print(*cards)

'''
7
0 0 0 0 0 0 0

6
1 0 1 0 0 0 

10
1 0 2 3 1 0 1 0 3 0

1
0

2
0 0
'''
