"""
Title : 전설의 JBNU
Link : https://www.acmicpc.net/problem/12757
"""

import sys
input = sys.stdin.readline
MIIS = lambda: map(int, input().split())


def bin_search(all_keys, key):
    global K, data
    min_dist = K + 1
    ans = -1
    left, right = 0, len(all_keys) - 1
    while left <= right:
        mid = (left + right) // 2
        mid_key = all_keys[mid]
        if abs(key - mid_key) == min_dist:
            ans = '?'
        elif abs(key - mid_key) < min_dist:
            ans = mid_key
            min_dist = abs(key - mid_key)
        if mid_key > key:
            right = mid - 1
        else:
            left = mid + 1
    return ans


if __name__ == "__main__":
    N, M, K = MIIS()
    data = {}
    for _ in range(N):
        k, v = MIIS()
        data[k] = v
    for _ in range(M):
        cmd = list(MIIS())
        if cmd[0] == 1:
            _, k, v = cmd
            data[k] = v
        elif cmd[0] == 2:
            _, k, v = cmd
            key = bin_search(sorted(data.keys()), k)
            if key == "?" or key == "-1":
                continue
            data[key] = v
        else:
            k = cmd[1]
            if k in data:
                print(k)
            else:
                ans = bin_search(sorted(data.keys()), k)
                if ans == "?" or ans == -1:
                    print(ans)
                else:
                    print(data[ans])
