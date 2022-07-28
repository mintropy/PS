"""
Title : 책 나눠주기
Link : https://www.acmicpc.net/problem/9576
"""
# Greedy
import heapq
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


if __name__ == "__main__":
    for _ in range(int(input())):
        N, M = MIIS()
        students = sorted([tuple(MIIS()) for _ in range(M)], reverse=True)
        heap, ans = [], 0
        for book in range(1, N + 1):
            while students and students[-1][0] == book:
                heapq.heappush(heap, students.pop()[1])
            while heap:
                if heapq.heappop(heap) >= book:
                    ans += 1
                    break
        print(ans)


# Bipartite Matching
import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def dfs(student):
    global students, books
    if visited[student]:
        return False
    visited[student] = True
    a, b = students[student]
    for book in range(a, b + 1):
        if not books[book] or dfs(books[book]):
            books[book] = student
            return True
    return False


if __name__ == "__main__":
    for _ in range(int(input())):
        N, M = MIIS()
        students = [[]] + [list(MIIS()) for _ in range(M)]
        books = [0] * (N + 1)
        for student in range(1, M + 1):
            visited = [False] * (M + 1)
            dfs(student)
        print(N + 1 - books.count(0))
