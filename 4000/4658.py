"""
Title : 삼각형 게임
Link : https://www.acmicpc.net/problem/4658
"""

import sys
input = sys.stdin.readline


def solution() -> None:
    """Main solution function
    """
    while True:
        triangles = [tuple(map(int, input().split())) for _ in range(6)]
        max_point = -1
        for i in range(6):
            for j in range(3):
                triangles_check = [False] * 6
                triangles_check[i] = True
                point = search(triangles, [triangles[i][j:] + triangles[i][:j]], 1, triangles_check)
                if max_point < point:
                    max_point = point
        if max_point == -1:
            print('none')
        else:
            print(max_point)

        cmd = input().strip()
        if cmd == '$':
            break


def search(triangles: list, comb_now: list, triangles_count: int, triangles_check: list) -> int:
    """DFS function

    Parameters
    ----------
    triangles : list
        input triangles list
    comb_now : list
    triangles_count : int
    triangles_check : list

    Returns
    -------
    int
        point of hexagon
    """
    if triangles_count == 6:
        if comb_now[0][0] == comb_now[-1][-1]:
            return calc_point(comb_now)
        return -1
    max_point = -1
    for i in range(6):
        if triangles_check[i]:
            continue
        for j in range(3):
            if comb_now[-1][-1] == triangles[i][j]:
                comb_now.append(triangles[i][j:] + triangles[i][:j])
                point = search(triangles, comb_now, triangles_count + 1, triangles_check)
                comb_now.pop()
                if max_point < point:
                    max_point = point
    return max_point


def calc_point(combinations: list) -> int:
    """calculate point of hexagon

    Parameters
    ----------
    combinations : list


    Returns
    -------
    int
    """
    return sum(combinations[i][1] for i in range(6))


solution()
