'''
Title : 숫자 카드
'''


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    cards = list(input())
    card_count = {}
    for card in cards:
        if int(card) in card_count:
            card_count[int(card)] += 1
        else:
            card_count[int(card)] = 1

    max_count_card = -1
    max_count = -1
    for key in card_count.keys():
        if card_count[key] >= max_count and key > max_count_card:
            max_count_card = key
            max_count = card_count[key]

    print(f'#{tc} {max_count_card} {max_count}')