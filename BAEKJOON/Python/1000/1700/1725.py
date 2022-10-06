"""
Title : 히스토그램
Link : https://www.acmicpc.net/problem/1725
"""

from sys import stdin

input = stdin.readline
II = lambda: int(input())

if __name__ == "__main__":
    N = II()
    histogram = [0] + [II() for _ in range(N)] + [0]
    stack = [0]
    ans = 0
    for i in range(1, N + 2):
        while stack and histogram[stack[-1]] > histogram[i]:
            h = stack.pop()
            ans = max(ans, histogram[h] * (i - stack[-1] - 1))
        stack.append(i)
    print(ans)


# ------------------------------------------------------------

from sys import stdin

input = stdin.readline
II = lambda: int(input())


def div_conquer(N: int, histogram: list[int], left: int, right: int) -> int:
    if left == right:
        return histogram[left]
    mid = (left + right) // 2
    l = r = mid
    h = histogram[mid]
    w = 1
    ans = h
    while l > left and r < right:
        if (h_l := histogram[l - 1]) >= (h_r := histogram[r + 1]):
            l -= 1
            w += 1
            h = min(h, h_l)
        else:
            r += 1
            w += 1
            h = min(h, h_r)
        ans = max(ans, h * w)
    while l > left:
        l -= 1
        w += 1
        h = min(h, histogram[l])
        ans = max(ans, w * h)
    while r < right:
        r += 1
        w += 1
        h = min(h, histogram[r])
        ans = max(ans, w * h)
    return max(
        ans,
        div_conquer(N, histogram, left, mid),
        div_conquer(N, histogram, mid + 1, right),
    )


if __name__ == "__main__":
    N = II()
    histogram = [II() for _ in range(N)]
    print(div_conquer(N, histogram, 0, N - 1))
