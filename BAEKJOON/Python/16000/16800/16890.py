"""
Title : 창업
Link : https://www.acmicpc.net/problem/16890
"""

from collections import deque
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    ko_alp = sorted(list(input().strip()))
    cu_alp = sorted(list(input().strip()), reverse=True)
    L = len(ko_alp)

    ko, cu = deque(ko_alp[: L - L // 2]), deque(cu_alp[: L // 2])
    ans = [""] * L
    l_idx, r_idx = 0, L - 1

    for t in range(L - 1):
        if ko[0] >= cu[0]:
            if t % 2:
                ans[r_idx] = cu.pop()
            else:
                ans[r_idx] = ko.pop()
            r_idx -= 1
        else:
            if t % 2:
                ans[l_idx] = cu.popleft()
            else:
                ans[l_idx] = ko.popleft()
            l_idx += 1
    if ko:
        ans[l_idx] = ko[0]
    else:
        ans[l_idx] = cu[0]
    print("".join(ans))
