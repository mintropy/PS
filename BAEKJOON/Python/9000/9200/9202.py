"""
Title : Boggle
Link : https://www.acmicpc.net/problem/9202
"""

from collections import deque
from sys import stdin

input = stdin.readline
II = lambda: int(input())
IS = lambda: input().strip()


if __name__ == "__main__":
    W: int = II()
    words: list[str] = [IS() for _ in range(W)]
    trie: dict[str:set] = {"": set()}
    for word in words:
        last: str = ""
        for s in word:
            if s not in trie[last]:
                trie[last].add(s)
                trie[last + s] = set()
            last += s

    input()
    B: int = II()
    for _ in range(B):
        boggle_board: list[str] = [IS() for _ in range(4)]
        score: int = 0
        max_len_word: str = ""
        words_count: set = set()

        delta: tuple[tuple[int]] = (
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
        )
        for i, line in enumerate(boggle_board):
            for j, s in enumerate(line):
                if s not in trie[""]:
                    continue
                queue: deque = deque([(i, j, s, {(i, j)})])
                x: int
                y: int
                s: str
                nx: int
                ny: int
                while queue:
                    x, y, s, visited = queue.popleft
                    if not trie[s]:
                        words_count.add(s)
                        continue
                    for dx, dy in delta:
                        nx, ny = i + dx, j + dy
                        if (nx, ny) in visited:
                            continue
                        if 0 <= nx < 4 and 0 <= ny < 4:
                            _s: str = boggle_board[nx][ny]
                            if _s not in trie[s]:
                                continue
                            queue.append((nx, ny, s + _s, visited + {(nx, ny)}))

        print(words_count)

        try:
            input()
        except Exception:
            break