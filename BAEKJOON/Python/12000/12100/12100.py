"""
Title : 2048 (Easy)
Link : https://www.acmicpc.net/problem/12100
"""

from sys import stdin

input = stdin.readline

Board = list[list[int]]


class Board:
    def __init__(self) -> None:
        self.max_value = 0

    def rotate(self, board: Board) -> list[Board]:
        board_list = [
            board,
            [line[::-1] for line in board],
            list(list(line) for line in zip(*board)),
            list(list(line) for line in zip(*[line for line in board[::-1]])),
        ]
        return board_list

    def move(self, board: Board) -> Board:
        new_board = []
        for line in board:
            new_line = [0] * len(line)
            idx = 0
            for x in line:
                if not x:
                    continue
                if not new_line[idx]:
                    new_line[idx] = x
                elif new_line[idx] == x:
                    new_line[idx] = x * 2
                    idx += 1
                else:
                    idx += 1
                    new_line[idx] = x
            new_board.append(new_line)
        return new_board

    def dfs(self, move_count: int, board: Board) -> None:
        if not move_count:
            if self.max_value < (tmp := max([max(line) for line in board])):
                self.max_value = tmp
            return
        for new_board in self.rotate(board):
            self.dfs(move_count - 1, self.move(new_board))


if __name__ == "__main__":
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    board2048 = Board()
    board2048.dfs(5, board)
    print(board2048.max_value)

"""
import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))


class Board:
    def __init__(self, board, n):
        self.size = n
        self.board = board
        self.max_block = 0

    def check(self, stack):
        '''
        이동하는 끝부분 부터 확인
        연속된 두 값이 같으면 두 값을 더하여 추가
        연속된 두 값이 다르면 개별로 추가
        '''
        idx = 0
        l = len(stack)
        tmp = []
        while idx < l:
            if idx == l - 1:
                tmp.append(stack[idx])
                idx += 1
            elif stack[idx] == stack[idx + 1]:
                tmp.append(stack[idx] * 2)
                idx += 2
            else:
                tmp.append(stack[idx])
                idx += 1
        return tmp

    def move_right(self, old_board: list) -> list:
        new_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            stack = []
            for j in range(self.size - 1, -1, -1):
                if old_board[i][j] != 0:
                    stack.append(old_board[i][j])
            next_num = self.check(stack)
            for j in range(len(next_num)):
                new_board[i][-1 -j] = next_num[j]
        return new_board
    
    def move_left(self, old_board: list) -> list:
        new_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            stack = []
            for j in range(self.size):
                if old_board[i][j] != 0:
                    stack.append(old_board[i][j])
            next_num = self.check(stack)
            for j in range(len(next_num)):
                new_board[i][j] = next_num[j]
        return new_board

    def move_down(self, old_board: list) -> list:
        new_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            stack = []
            for j in range(self.size - 1, -1, -1):
                if old_board[j][i] != 0:
                    stack.append(old_board[j][i])
            next_num = self.check(stack)
            for j in range(len(next_num)):
                new_board[-1 -j][i] = next_num[j]
        return new_board

    def move_up(self, old_board: list) -> list:
        new_board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        for i in range(self.size):
            stack = []
            for j in range(self.size):
                if old_board[j][i] != 0:
                    stack.append(old_board[j][i])
            next_num = self.check(stack)
            for j in range(len(next_num)):
                new_board[j][i] = next_num[j]
        return new_board

    def find_max_block(self, check_board):
        max_block = 0
        for i in range(self.size):
            if max(check_board[i]) > max_block:
                max_block = max(check_board[i])
        return max_block

    def dfs(self, count, board):
        # 중간중간 확인하는 방법으로 시간 단축할 수 있지만,
        # 우선은 5회 기준으로 확인
        if count == 5:
            block = self.find_max_block(board)
            if self.max_block < block:
                self.max_block = block
            return
        # 기존 2048보드판을 4방향으로 이동 후 탐색
        self.dfs(count + 1, self.move_right(board))
        self.dfs(count + 1, self.move_left(board))
        self.dfs(count + 1, self.move_down(board))
        self.dfs(count + 1, self.move_up(board))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

board2048 = Board(board, n)
board2048.dfs(0, board2048.board)
print(board2048.max_block)
"""
