"""
Title : Boggle
Link : https://www.acmicpc.net/problem/9202
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())
IS = lambda: input().strip()

Vector = tuple[int]


class Node:
    def __init__(self) -> None:
        self.last: bool = False
        self.child: dict = {}

    def add_node(self, string: str) -> None:
        current = self
        for s in string:
            if s not in current.child:
                current.child[s] = Node()
            current = current.child[s]
        current.last = True


def search(x: int, y: int, string: str, node: Node):
    global trie, words_count, delta, boggle_board
    if node.last:
        words_count.add(string)
    visited[x][y] = True
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if visited[nx][ny]:
                continue
            if (s := boggle_board[nx][ny]) in node.child:
                search(nx, ny, string + s, node.child[s])
                pass
    visited[x][y] = False


if __name__ == "__main__":
    W: int = II()
    trie = Node()
    for _ in range(W):
        string = IS()
        trie.add_node(string)

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
    visited = [[False] * 4 for _ in range(4)]

    input()
    B: int = II()
    ans = ""
    for k in range(B):
        boggle_board: tuple[str] = tuple(IS() for _ in range(4))
        words_count: set[str] = set()
        for i, line in enumerate(boggle_board):
            for j, s in enumerate(line):
                if s in trie.child:
                    search(i, j, s, trie.child[s])

        words_count = sorted(words_count, key=lambda x: (-len(x), x))
        score: int = sum([words_point[len(x)] for x in words_count])
        max_len_word: str = words_count[0]
        ans += f"{score} {max_len_word} {len(words_count)}\n"
        if k == B - 1:
            break
        input()
    print(ans)

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
