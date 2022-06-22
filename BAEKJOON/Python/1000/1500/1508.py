"""
Title : 레이스
Link : https://www.acmicpc.net/problem/1508
"""

from sys import stdin

input = stdin.readline
MIIS = lambda: map(int, input().split())


def find_dist(N: int, M: int, K: int, pos: list[int]) -> int:
    left, right = 0, N
    dist = 0
    while left <= right:
        mid = (left + right) // 2
        count = check_dist(mid, K, pos)
        if count >= M:
            dist = mid
            left = mid + 1
        else:
            right = mid - 1
    return dist


def check_dist(dist: int, K: int, pos: list[int]) -> int:
    idx = 1
    p = pos[0]
    count = 1
    while idx < K:
        if pos[idx] - p >= dist:
            count += 1
            p = pos[idx]
        idx += 1
    return count


def find_answer(M: int, K: int, pos: list[int], dist: int) -> list[int]:
    ans = [0] * K
    ans[0] = 1
    p = pos[0]
    count = 1
    for i in range(1, K):
        if count == M:
            break
        if pos[i] - p >= dist:
            ans[i] = 1
            count += 1
            p = pos[i]
    return ans


if __name__ == "__main__":
    N, M, K = MIIS()
    possible_positions = list(MIIS())
    max_dist = find_dist(N, M, K, possible_positions)
    ans = find_answer(M, K, possible_positions, max_dist)
    for x in ans:
        print(x, end="")


"""
레이스 트랙 길이 N 직선, 심판 M명 적절한 곳에 배치
심판은 아무 곳에나 배치 ㄴㄴ, 정해진 K개 곳에만 가능
심판 배치, 가장 가까운 두 심판의 거리 최대로

M명을 배치할 수 있는 최대 거리를 찾아야 함

1. find_dist : binary search로 최대 거리 찾기
    find_dist에서 check_dist 함수를 호출, 
    특정 거리에서 최대 배치 가능한 심판 수를 탐색
2. M명을 배치하는 최대 거리를 탐색하게 되고
3. 해당 거리(max_dist)를 기준으로 정답 탐색
    사전식으로 빠른 순 -> 1이 최대한 앞으로 오도록 탐색하여 출력
"""
