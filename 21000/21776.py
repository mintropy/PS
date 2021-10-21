"""
Title : 가희와 읽기 쓰기 놀이
Link : https://www.acmicpc.net/problem/21776
"""

import sys
input = sys.stdin.readline


def dfs(word_now: str):
    global n, turn, cards, possible_output
    # 다음사람 카드 내는 것 탐색
    turn_left = False
    for i in range(n):
        # 더 낼수 있는 카드가 없다면
        if not turn[i]:
            continue
        # 아니라면 카드 내기
        turn_left = True
        next_card = turn[i].pop()
        next_word = calc_card(word_now, cards[next_card])
        if next_word == 'ERROR':
            possible_output.add(next_word)
            continue
        dfs(next_word)
        turn[i].append(next_card)
    # 더 낼 수 있는 카드가 없다면
    if not turn_left:
        possible_output.add(word_now)
        return


def calc_card(word_now: str, card_set: list) -> str:
    for c in card_set:
        cmd, x = c.split()
        if cmd == 'ADD':
            word_now += x
        elif cmd == 'DEL':
            x = int(x)
            if x >= len(word_now):
                return 'ERROR'
            word_now = word_now[:x] + word_now[x + 1:]
    return word_now


n, c = map(int, input().split())
turn = []
for _ in range(n):
    _, *act = map(int, input().split())
    turn.append(act[::-1])

cards = [()]
for _ in range(c):
    cards_list = list(input().strip().split(','))
    cards.append(cards_list)

possible_output = set()

dfs('')
print(*sorted(possible_output), sep='\n')
