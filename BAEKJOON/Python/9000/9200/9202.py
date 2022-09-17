"""
Title : Boggle
Link : https://www.acmicpc.net/problem/9202
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
IS = lambda: input().strip()

Vector = tuple[int]


def search(x: int, y: int, string: str, visited: set):
    global trie, words_count, delta, boggle_board
    if string not in trie:
        return
    if trie[string][1]:
        words_count.add(string)
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if (nx, ny) in visited:
            continue
        if 0 <= nx < 4 and 0 <= ny < 4:
            search(
                nx,
                ny,
                string + boggle_board[nx][ny],
                visited | {(nx, ny)},
            )


if __name__ == "__main__":
    W: int = II()
    words: list[str] = [IS() for _ in range(W)]
    trie = {"": [set(), False]}
    for word in words:
        last_word: str = ""
        for s in word:
            next_word: str = last_word + s
            trie[last_word][0].add(s)
            if next_word not in trie:
                trie[next_word] = [set(), False]
            last_word = next_word
        trie[last_word][1] = True

    words_point: Vector = (0, 0, 0, 1, 1, 2, 3, 5, 11)
    delta: tuple[Vector] = (
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    )

    input()
    B: int = II()
    for k in range(B):
        boggle_board: tuple[str] = tuple(IS() for _ in range(4))
        words_count: set[str] = set()
        for i, line in enumerate(boggle_board):
            for j, s in enumerate(line):
                search(i, j, s, {(i, j)})

        words_count = sorted(words_count, key=lambda x: (-len(x), x))
        score: int = sum([words_point[len(x)] for x in words_count])
        max_len_word: str = words_count[0]
        print(score, max_len_word, len(words_count))
        if k == B - 1:
            break
        else:
            input()

"""
3
ABAA
ABAB
ZZZ

1
AAAB
AAAB
AAAB
ZZZB

"""
