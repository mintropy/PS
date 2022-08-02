"""
Title : 모노미노도미노2
Link : https://www.acmicpc.net/problem/20061
"""

from sys import stdin


input = stdin.readline
Block = tuple[tuple[int]]


def move_blocks(blocks: Block) -> int:
    global board
    points = 0
    green_pos = move_single_block(blocks, True)
    blue_pos = move_single_block(blocks, False)
    points += push_blocks(green_pos, True)
    points += push_blocks(blue_pos, False)
    return points


def move_single_block(blocks: Block, is_green: bool) -> Block:
    def check_board(blocks: Block, is_green: bool) -> bool:
        for x, y in blocks:
            if is_green and x >= 10:
                return False
            elif not is_green and y >= 10:
                return False
        return True

    while True:
        if is_green:
            next_blocks = tuple((x + 1, y) for x, y in blocks)
        else:
            next_blocks = tuple((x, y + 1) for x, y in blocks)
        if not check_board(next_blocks, is_green):
            return blocks
        if not check_blocks(next_blocks):
            return blocks
        blocks = next_blocks


def check_blocks(blocks: Block) -> bool:
    global board
    for x, y in blocks:
        if board[x][y]:
            return False
    return True


def push_blocks(blocks: Block, is_green: bool) -> int:
    global board
    points = 0
    for x, y in blocks:
        board[x][y] = 1
    for i in range(6, 10):
        if check_line(i, is_green):
            points += 1
            pull_lines(i, is_green)
    for i in range(4, 6):
        for j in range(4):
            if is_green:
                if board[i][j]:
                    pull_lines(9, True)
                    break
            else:
                if board[j][i]:
                    pull_lines(9, False)
                    break
    return points


def check_line(line_idx: int, is_green: bool) -> bool:
    global board
    for j in range(4):
        if is_green:
            if board[line_idx][j]:
                continue
            return False
        else:
            if board[j][line_idx]:
                continue
            return False
    for j in range(4):
        if is_green:
            board[line_idx][j] = 0
        else:
            board[j][line_idx] = 0
    return True


def pull_lines(line_idx: int, is_green: bool) -> None:
    global board
    for i in range(line_idx - 1, 2, -1):
        for j in range(4):
            if is_green:
                board[i + 1][j] = board[i][j]
            else:
                board[j][i + 1] = board[j][i]


def count_blocks() -> int:
    global board
    count = 0
    for i in range(6, 10):
        for j in range(4):
            if board[i][j]:
                count += 1
            if board[j][i]:
                count += 1
    return count


if __name__ == "__main__":
    board = [[0] * 10 for _ in range(10)]
    points = 0
    for _ in range(int(input())):
        t, x, y = map(int, input().split())
        if t == 1:
            blocks = ((x, y),)
        elif t == 2:
            blocks = ((x, y), (x, y + 1))
        elif t == 3:
            blocks = ((x, y), (x + 1, y))
        points += move_blocks(blocks)
    print(points)
    print(count_blocks())

"""
9
2 1 0
2 1 0
2 1 0
2 1 0
2 1 0
3 0 2
3 0 2
3 0 3
3 0 3
ans:
4
8
"""
